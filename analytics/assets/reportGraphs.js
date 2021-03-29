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
			module: ""
		}

		this.getDetails = this.getDetails.bind(this)
	}

	componentDidMount(){
		this.getDetails()
	}

	getDetails(){
		axios.get(`http://127.0.0.1:8002/analytics/get-details/`)
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
				<Template data={ this.state.data } module={ this.state.module }/>
  			</React.Fragment>)
	}
}

export default ReportGraphs

if (document.getElementById('report-graphs')) {
    ReactDOM.render(<ReportGraphs />, document.getElementById('report-graphs'));
}