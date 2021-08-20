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
			graphid: "all",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
	}

	componentDidMount(){
		const baseUrl = document.getElementById("baseUrl").value
		var module_i = ""
		if(document.getElementById('module')){
			module_i = document.getElementById('module').value
		}
		 
		var graphid = "all"

		if(this.props.module){
			module_i = this.props.module
		}

		if(this.props.graphid){
			// console.log("graph has props ")
			// console.log(this.props.graphid)
			graphid = this.props.graphid

		}
		

		this.setState({
			baseUrl: baseUrl,
			module: module_i,
			graphid: graphid
		},()=>{
			this.getDetails()
		})
	}

	getDetails(){
		axios.get(`${this.state.baseUrl}/analytics/get-details/`)
        	.then(response => {
        		// console.log("response is ")
        		// console.log(response.data)
        		// console.log("graph is ")
        		// console.log(this.state.graphid)
        		
          this.setState({
            data: response.data
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}


	render(){
		return (<React.Fragment>
				<Template data={ this.state.data } graphid={this.state.graphid} module={ this.state.module } view={ this.state.view } baseUrl={this.state.baseUrl}/>
  			</React.Fragment>)
	}
}

export default ReportGraphs

if (document.getElementById('report-graphs')) {
    ReactDOM.render(<ReportGraphs />, document.getElementById('report-graphs'));
}