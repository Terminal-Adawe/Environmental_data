import React from 'react';
import ReactDOM from "react-dom";
import Template from './template';

import axios from "axios";
import cookie from "react-cookies";

class Reports extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			module: "",
			view: "graph",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			url: '/analytics/get-reports/'
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
	}

	componentDidMount(){
		const baseUrl = document.getElementById("baseUrl").value

		this.setState({
			baseUrl: baseUrl
		},()=>{
			this.getDetails()
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
		return (<React.Fragment>
				<Template data={ this.state.data } module={ this.state.module } view={ this.state.view } baseUrl={this.state.baseUrl}/>
  			</React.Fragment>)
	}
}

export default Reports

if (document.getElementById('report_list')) {
    ReactDOM.render(<Reports />, document.getElementById('report_list'));
}