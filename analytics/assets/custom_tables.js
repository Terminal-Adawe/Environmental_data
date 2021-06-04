import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

import Axis from './axis';
import FormulateReportData from './formulateReport';
import Test from './test';




class CustomTables extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			username: "",
			module: "all",
			table_name: "",
			moduleid: "",
			x_column: "",
			y_column: "",
			groupType: "sum",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			valueType: "",
			get_report_url: "/analytics/get-tables/",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
	}

	componentDidMount(){

		console.log("component mounted")

		const baseUrl = document.getElementById("baseUrl").value
		const username = document.querySelector(".username").value

		this.setState({
			baseUrl: baseUrl,
			username: username
		},()=>{
			this.getDetails()
		})
	}

	getDetails(){
		const url = this.state.get_report_url

		axios.get(`${this.state.baseUrl}${url}`)
        	.then(response => {
        		console.log("response is ")
        		console.log(response)
          this.setState({
            data: response.data.Custom_table,
          })
        })
        .catch(error => {
          // here catch error messages and show them 
          console.log(error)
     	})
	}


	render(){
		return (<React.Fragment>
		{
			this.state.data.map((table,i)=>{
				console.log("table is ")
				console.log(table)
				return <section key={i} className="panel">
				<header className="panel-heading">
					<div className="panel-actions">
						<a href="#" className="fa fa-caret-down"></a>
					</div>
		
					<h2 className="panel-title">{table.table_name}</h2>
				</header>
				<div className="panel-body">
					<FormulateReportData username={this.state.username} module_name={table.module} x_column={table.x_column} y_column={table.y_column} valueType={table.value} table_name={table.table_name} groupType={table.group_type} description={table.description} />
				</div>
			</section>
			})
			
		}
			
			</React.Fragment>)
	}
}

export default CustomTables

if (document.getElementById('custom-tables')) {
	console.log("ID INTACT")
    ReactDOM.render(<CustomTables />, document.getElementById('custom-tables'));
}