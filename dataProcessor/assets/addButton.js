import React from 'react';
import ReactDOM from 'react-dom';
import axios from "axios";
import cookie from "react-cookies";


class AddButton extends React.Component {
	constructor(){
		super()

		this.state={
			type: "",
			description: "",
		}

		this.getFormData = this.getFormData.bind(this)
		this.insertData = this.insertData.bind(this)

	}

	componentDidMount(){

		if(this.props.states.formtype=="education"){
			this.setState({
				type: this.props.states.formtype,
				description: "Education",
			})
		} else if (this.props.states.formtype=="professional"){
			this.setState({
				type: this.props.states.formtype,
				description: "Professional Experience"
			})
		}
	}

	getFormData(){		

		console.log("Info sent is ")
		console.log(this.props.states.form)

        this.props.loader(true)
		this.insertData(this.props.states.form)
	}

	insertData(formData){

        // var axios = require('axios');

        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

        const url = this.props.states.url
        const baseUrl = this.props.baseUrl

		axios.post(`${baseUrl}/api/${url}`,formData,{
                headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken")
                 },
            }
            )
      .then(response => {
        console.log("Response generated is ")
        console.log(response)
        this.props.loader(false)
        if(response.status == "201"){
        	console.log(response.statusText)
        	console.log("Set everything to empty")
        	var inputs = document.querySelectorAll('.input-element')
        	let count_p = 0 
        	let count_d = 0

            inputs.forEach((input,i)=>{
              
                    input.value = ""
                
            })

        	this.props.updateEntries(formData)

        } else {
        	console.log(response.data.message)
        	document.getElementById('message').innerHTML = response.data.message
        }

      })
      .catch(error => {
        this.props.loader(false)
        console.log(error)
        document.getElementById('message').innerHTML = error
        // console.log("an error occurred!!")
      })
	}

	render(){

		return (<button type="button" className="stylessbutton addtab my-4" id="add" onClick={this.getFormData}><img src="https://img.icons8.com/officel/40/000000/add.png"/> Add { this.state.description }</button>
            )
	}
}

export default AddButton;

