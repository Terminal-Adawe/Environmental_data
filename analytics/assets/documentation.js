import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

import { Route, Link, Switch, BrowserRouter as Router } from "react-router-dom"; 

class Documentation extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			module: "",
			view: "graph",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			url: '/analytics/add-report/'
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
		this.addReportBtn = this.addReportBtn.bind(this)
	}

	componentDidMount(){
		const baseUrl = document.getElementById("baseUrl").value

		this.addReportBtn()

		this.setState({
			baseUrl: baseUrl
		})
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
		return (<div className=""></div>)
	}
}

export default Documentation

if (document.getElementById('documentation')) {
    ReactDOM.render(<Documentation />, document.getElementById('documentation'));
}