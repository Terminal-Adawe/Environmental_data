import React from 'react';
import ReactDOM from "react-dom";
import Template from './template';

import axios from "axios";
import cookie from "react-cookies";


class Index extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			module: "all",
			baseUrl: "http://3.9.132.4",
		}

		this.getDetails = this.getDetails.bind(this)
	}

	componentDidMount(){
		this.getDetails()
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
				<Template data={ this.state.data } module={ this.state.module }/>
  			</React.Fragment>)
	}
}

export default Index

if (document.getElementById('dashboard-graphs')) {
    ReactDOM.render(<Index />, document.getElementById('dashboard-graphs'));
}