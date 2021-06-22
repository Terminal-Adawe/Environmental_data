import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

class SaveBtn extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			module: "",
			type: "graph",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			url: '/analytics/save/'
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
		this.saveBtnClick = this.saveBtnClick.bind(this)
	}

	componentDidMount(){
		const baseUrl = document.getElementById("baseUrl").value
		// const type = document.querySelector(".save_button_type").value

		console.log("Props are ")
		console.log(this.props.type)

		this.setState({
			baseUrl: baseUrl,
			type: this.props.type
		})
	}

	saveBtnClick(e){
		var report_value = this.state.type

		console.log("Value is ")
		console.log(report_value)
	}

	getDetails(){
		const url = this.state.url

		axios.get(`${this.state.baseUrl}${url}`)
        	.then(response => {
        		console.log("reports response is ")
        		console.log(response.data)
        		var module_i = document.getElementById('module').value
          this.setState({
            data: response.data,
            module: module_i
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}


	render(){
		return (<button className="btn btn-info" type="button" onClick={ this.saveBtnClick } >Save { this.state.type }</button>)
	}
}

export default SaveBtn

const save_classes = document.querySelectorAll('.save_button')

if (document.querySelectorAll('.save_button')) {
		for(var sc=0; sc<save_classes.length; sc++){
			var type = save_classes[sc].previousElementSibling
			ReactDOM.render(<SaveBtn type={ type.value }/>, save_classes[sc]);
		}
    
}