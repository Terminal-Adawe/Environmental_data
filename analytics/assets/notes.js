import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";


class Notes extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			get_notes: '/api/analytics/get-notes/'
			// baseUrl: "http://localhost:8002",
		}

		this.getNotes = this.getNotes.bind(this)
	}

	componentDidMount(){

		let notes_id = ""

		if(this.props.notes_id){
			notes_id = this.props.notes_id
		} else {
			notes_id = document.querySelector(".notes_id").value
		}

		this.getNotes(notes_id)
	}


	getNotes(notes_id){
		const url = this.state.get_notes

		axios.get(`${this.state.baseUrl}${url}`,
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





	render(){
		return (
				<div className="container-fluid">
					{
						this.state.data.map((note,i)=>{
							<div className="row">
								<div className="container-fluid">
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