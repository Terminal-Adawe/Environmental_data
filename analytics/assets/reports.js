import React from 'react';
import ReactDOM from "react-dom";
import Template from './template';

import axios from "axios";
import cookie from "react-cookies";
import ModalPortal from './modalPortal';

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
		this.addToReport = this.addToReport.bind(this)

		this.buttonRef = React.createRef();
	}

	componentDidMount(){
		const baseUrl = document.getElementById("baseUrl").value

		this.setState({
			baseUrl: baseUrl
		},()=>{
			this.getDetails()

			if(this.buttonRef.current){
				this.buttonRef.current.addEventListener('click', () => this.addToReport);
			}
		})
	}

	componentDidUpdate(prevState){
		if(this.state.data != prevState.data){
			console.log("Component updated")
			if(this.buttonRef.current){
				console.log("Button exists")
				this.buttonRef.current.addEventListener('click', () => this.addToReport, { capture: true });
			}
			
		}
		
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

		addToReport(){
			console.log("Report name is ")
			console.log(report_name)
		}


	render(){
		return (<div className="container-fluid">
							<div className="row">
								<div className="col-lg-12 col-12">
									<h3>Select a report to add to</h3>
								</div>
							</div>
					{
						this.state.data ? this.state.data.map((report,i)=>{
							console.log("report is ")
							console.log(report)
							return <div className="row my-2" key={i} style={{ 'paddingBottom':'8px' }}>
												<div className="col-lg-12 col-md-12 col-sm-12 col-12">
														<button className="btn addToReport_btn" ref={this.buttonRef} onClick={()=>this.addToReport} type="button">{ report.report_name }</button>
												</div>
											</div>
						}) : ""
					}
  			</div>)
	}
}

export default Reports

if (document.getElementById('report_list')) {
    ReactDOM.render(<Reports />, document.getElementById('report_list'));
}