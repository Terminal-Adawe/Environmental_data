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
        		// var module_i = document.getElementById('module').value
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
							<div className="row">
								<div className="col-lg-12 col-12">
									<h3>Select a report to add to</h3>
								</div>
							</div>
					{
						this.state.data ? this.state.data.map((report,i)=>{
							console.log("report is ")
							console.log(report)
							return <div className="row"><div className="col-lg-12 col-12"><a href="#">{ report.report_name }</a></div>
											</div>

						}) : ""
					}
  			</React.Fragment>)
	}
}

export default Reports

if (document.getElementById('report_list')) {
    ReactDOM.render(<Reports />, document.getElementById('report_list'));
}