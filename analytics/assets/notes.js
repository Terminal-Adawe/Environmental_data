import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";


class Notes extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			get_notes: '/analytics/get-notes/',
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
		}

		this.getNotes = this.getNotes.bind(this)
	}

	componentDidMount(){

		let notes_id = ""
		const baseUrl = document.getElementById("baseUrl").value

		if(this.props.notes_id){
			notes_id = this.props.notes_id
		} else {
			notes_id = document.querySelector(".notes_id").value
		}

		this.setState({
			baseUrl: baseUrl,
		},()=>{
			this.getNotes(notes_id)
		})

		
	}

	


	getNotes(notes_id){
		const baseUrl = this.state.baseUrl
  	const url = this.state.get_notes

  	if(typeof(notes_id)=="string" && (notes_id.indexOf("above") != -1)){

  	} else {
  		axios.get(`${baseUrl}${url}`,
							{
							params: {
								id: notes_id
							}
							},{
                headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                 },
            })
        	.then(response => {
        		console.log("The notes response is ")
        		console.log(response.data)
          	this.setState({
            	data: response.data,
          	})

          	this.props.updateNotes(response.data, "add")
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
  	}
		
	}





	render(){
		return (
				<div className="container-fluid">
					{
						this.state.data.map((note,i)=>{
							return <div className="row">
								<div className="container-fluid note-font">
									<p>
										{ note.notes }
									</p>
								</div>
							</div>
						})
					}
				</div>
			)
	}
}

export default Notes


if (document.getElementById('Notes')) {
		 ReactDOM.render(<Notes />, document.getElementById('Notes'));
    
}