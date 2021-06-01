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

		this.handleSaveTableClick = this.handleSaveTableClick.bind(this)
		this.saveTable = this.saveTable.bind(this)
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




	handleSaveTableClick(){
		const module_ = this.state.module
		const x_column = this.state.x_column
		const y_column = this.state.y_column
		const valueType = this.state.valueType
		const groupType = this.state.groupType
		const table_name = this.state.table_name
		const username = this.state.username

		this.saveTable(username,table_name,module_,x_column,y_column,valueType,groupType)
	}

	saveTable(username,table_name,module_, x_column, y_column, valueType, groupType){
        let form_data = new FormData();

        const url = this.state.add_report_url
        const baseUrl = this.state.baseUrl


        console.log("sending info ... ")
        console.log(module_+" + "+x_column+" + "+y_column+" + "+valueType+" + "+groupType)
        console.log("Base url is ")
        console.log(this.state.baseUrl)

        form_data.append('username', username)
        form_data.append('table_name', table_name)
        form_data.append('module', module_)
        form_data.append('x_column', x_column)
        form_data.append('y_column', y_column)
        form_data.append('value', valueType)
        form_data.append('groupType', groupType)

        axios.post(`${baseUrl}/api/${url}`,form_data,{
                headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                 },
            }
            )
      .then(response => {
        console.log("Response generated is ")
        console.log(response.data)
        // this.props.loader(false)

        response.data.map((resp,i)=>{
            console.log(resp)
        })

        // Response is successful
        if(response.status == "201"){
            console.log(response.statusText)

            window.scrollTo({top: 0, behavior: 'smooth'});
           
            document.getElementById('success-message').innerHTML = "Successful"
            setTimeout(function(){
                document.getElementById('success-message').innerHTML = ""
            },4000)

        } else // response failed
        {
            document.getElementById('error-message').innerHTML = response.data.message
            console.log(response.data.message)
            setTimeout(function(){
               document.getElementById('error-message').innerHTML = ""
            },10000)
        }

      })
      .catch(error => {
        this.props.loader(false)
        console.log(error)
        document.getElementById('error-message').innerHTML = error
        setTimeout(function(){
             document.getElementById('error-message').innerHTML = ""
        },10000)
        // console.log("an error occurred!!")
      })
    }


	render(){
		// console.log("INSTANCE")
		// console.log(this.state.data)
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
					<Test username={this.state.username} module_name={table.module} x_column={table.x_column} y_column={table.y_column} valueType={table.value} table_name={table.table_name} groupType={table.group_type} />
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