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
        let form_data = new FormData();

        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

        this.props.getLocation

        // inputs.forEach((input,i)=>{
              
        //             input.value = ""
        //             form_data.append(input.name, input.value)
                
        //     })

        // Looping through object
        for (var key in formData) {
            if (formData.hasOwnProperty(key)) {
                console.log(key + " -> " + formData[key]);
                form_data.append(key, formData[key])
            }
        }

        // form_data.append('image', formData.image);
        // form_data.append('location', formData.location);

        console.log("User Location is ")
        console.log(form_data)
        console.log(" and ")
        console.log(formData.image)

        const url = this.props.states.url
        const image_url = this.props.states.image_url
        const baseUrl = this.props.baseUrl

        console.log("base url is ")
        console.log(baseUrl)

		axios.post(`${baseUrl}/api/${url}`,form_data,{
                headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                 },
            }
            )
      .then(response => {
        console.log("Response generated is ")
        console.log(response)
        this.props.loader(false)

        // Response is successful
        if(response.status == "201"){
        	console.log(response.statusText)
        	
        	var inputs = document.querySelectorAll('.input-element')
        	let count_p = 0 
        	let count_d = 0


             for(var i = 0; i<formData.image.length; i++){
                this.props.loader(true)

                let form_data_2 = new FormData();
                form_data_2.append('username', formData.username)
                form_data_2.append('report_id', response.data.id)
                form_data_2.append('module_id', response.data.module)
                form_data_2.append('image', formData.image[i])

                console.log("image file is ")
                console.log(formData.image[i])
                axios.post(`${baseUrl}/api/${image_url}`,form_data_2,{
                    headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                     enctype: 'multipart/form-data'
                    },
                })
                .then(response => {
                    console.log("Image response is ")
                    console.log(response)
                    this.props.loader(false)

                    if(response.status == "201"){
                        // Successful upload
                    } else {
                        // Failed upload
                    }

                })
                .catch(error => {
                    this.props.loader(false)
                    console.log(error)
                    document.getElementById('error-message').innerHTML = error
                    setTimeout(function(){
                        document.getElementById('error-message').innerHTML = ""
                    },10000)
                // console.log("an error occurred!!")
                })
             }
            
             document.getElementById('success-message').innerHTML = "Data successfully inserted"

             console.log("Set everything to empty")
            // Set everythinng to empty
            inputs.forEach((input,i)=>{
              
                    input.value = ""
                
            })

        	this.props.updateEntries(formData)

            setTimeout(function(){
                document.getElementById('success-message').innerHTML = ""
            },4000)

        } else // response failed
        {
            document.getElementById('error-message').innerHTML = response.data.message
        	console.log(response.data.message)
            setTimeout(function(){
        	   document.getElementById('error-message').innerHTML = ""
            },10000)
        }

      })
      .catch(error => {
        this.props.loader(false)
        console.log(error)
        document.getElementById('error-message').innerHTML = error
        setTimeout(function(){
             document.getElementById('error-message').innerHTML = ""
        },10000)
        // console.log("an error occurred!!")
      })

      
      
	}

	render(){

		return (<button type="button" className="stylessbutton addtab my-4" id="add" onClick={this.getFormData}><img src="https://img.icons8.com/officel/40/000000/add.png"/> Add { this.state.description }</button>
            )
	}
}

export default AddButton;

