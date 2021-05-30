import React from 'react';
import ReactDOM from "react-dom";
import Template from './template';

import axios from "axios";
import cookie from "react-cookies";

class ReportGraphs extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			module: "",
			view: "graph",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
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
		axios.get(`${this.state.baseUrl}/analytics/get-details/`)
        	.then(response => {
        		console.log("response is ")
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
				<Template data={ this.state.data } module={ this.state.module } view={ this.state.view }/>
  			</React.Fragment>)
	}
}

export default ReportGraphs

if (document.getElementById('report-graphs')) {
    ReactDOM.render(<ReportGraphs />, document.getElementById('report-graphs'));
}