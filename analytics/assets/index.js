import React from 'react';
import ReactDOM from "react-dom";
import Template from './template';

import axios from "axios";
import cookie from "react-cookies";

import '../node_modules/react-vis/dist/style.css';


class Index extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			module: "all",
			view: "dashboard",
			graphid: "all",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
	}

	componentDidMount(){
		const baseUrl = document.getElementById("baseUrl").value

		console.log("Base url is ")
		console.log(baseUrl)

		this.setState({
			baseUrl: baseUrl
		},()=>{
			this.getDetails()

			axios.defaults.baseURL = ""
		})
	}

	getDetails(){
		axios.get(`${this.state.baseUrl}/analytics/get-details/`)
        	.then(response => {
        		console.log("response is ")
        		console.log(response.data)
          this.setState({
            data: response.data,
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}


	render(){
		return (<React.Fragment>
				<div className="container">
					<div className="row">
						<div className="col-12">
							<h2>Dashboard</h2>
						</div>
					</div>
				</div>
				<Template data={ this.state.data } graphid={this.state.graphid} module={ this.state.module } view={ this.state.view }/>
  			</React.Fragment>)
	}
}

export default Index

if (document.getElementById('dashboard-graphs')) {
    ReactDOM.render(<Index />, document.getElementById('dashboard-graphs'));
}