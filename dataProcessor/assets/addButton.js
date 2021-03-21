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

        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

        const url = this.props.states.url

		axios.post(`http://127.0.0.1:8002/api/${url}`,formData,{
                headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken")
                 },
            }
            )
      .then(response => {
        console.log("Response is ")
        console.log(response)
        this.props.loader(false)
        if(response.status == "200"){
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
        console.log(error)
      })
	}

	render(){

		return (<button type="button" className="stylessbutton addtab my-4" id="add" onClick={this.getFormData}><img src="https://img.icons8.com/officel/40/000000/add.png"/> Add { this.state.description }</button>
            )
	}
}

export default AddButton;

