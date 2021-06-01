import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

import Axis from './axis';
import FormulateReportData from './formulateReport';




class TableBuilder extends React.Component {
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
			add_report_url: "add/save-table/",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)

		this.handleInputChanged = this.handleInputChanged.bind(this)
		this.handleAxisChanged = this.handleAxisChanged.bind(this)
		this.handleCheckboxInputChanged = this.handleCheckboxInputChanged.bind(this)
		this.handleGraphInputChanged = this.handleGraphInputChanged.bind(this)
		this.handleChartChange = this.handleChartChange.bind(this)
		this.handleOptionChange = this.handleOptionChange.bind(this)
		this.handleSaveTableClick = this.handleSaveTableClick.bind(this)
		this.saveTable = this.saveTable.bind(this)

		this.getData = this.getData.bind(this)
	}

	componentDidMount(){

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
		axios.get(`${this.state.baseUrl}/analytics/get-module-details/`)
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

	getData(data){
		this.setState({
			data: data
		})
	}

	handleInputChanged(e, name){
		const value = e.target.value

		console.log("Setting module id to "+e.target.value)

		this.setState({
			[name]: value
		},()=>{
			if(name=="module"){
				console.log("Module that is changed ")
				console.log(name)
				this.setState({
					x_column: "",
					y_column: "",
					valueType: ""
				})
			}

		})
	}

	handleGraphInputChanged(e){
		const value = e.target.value

		console.log("Setting module id to "+e.target.value)

	}

	handleCheckboxInputChanged(e){
		const value = e.target.value

		console.log("Setting module id to "+e.target.value)

	}

	handleAxisChanged(e, name){
		const value = e.target.value

		console.log("value is "+value+" and name is "+name)

		this.setState({
			[name]: value
		})


	}

	handleChartChange(e){
		this.setState({
			chartType: e.target.value
		})
	}

	handleOptionChange(e){
		console.log("Input changed from ")
		console.log(this.state.valueType)
		console.log(" to ")
		console.log(e.target.value)
		this.setState({
    		groupType: e.target.value
  		});
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
		return (<div className="row">
						<div className="col-lg-9 col-md-10 col-sm-12">
							<div className="row mt-2">
								<div className="col-12">
									<label><h4>Table Name</h4></label>
									<input 
										type="text" 
										id="table_name" 
										placeholder="Enter name of the table" 
										name="table_name" 
										className="input-element" 
										onChange={(e)=>this.handleInputChanged(e,"table_name")}
										 />
								</div>
							</div>

							<div className="row mt-2">
								<div className="col-lg-4 col-md-4 col-sm-12">
									<label><h5>Select Table to prepare report on</h5></label>
									<select id="module" name="module" defaultValue="1" className="input-element" onChange={(e)=>this.handleInputChanged(e,"module")}>
										<option value=""></option>
									{	
										this.state.data.modules ?
									
										this.state.data.modules.map((module,i)=>{
											return <option key={i} value={ module.id }>{ module.module_name }</option>
										})
									
										: "" 
									}
                    				  </select>
                    			</div>
                    			<Axis graphbuilder={ this.state.data.Graph_builder_field } title="Rows" name="y_column" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.module } valueType={ this.state.y_column } columnLength="col-lg-4 col-md-4 col-sm-6"/>

                    			<Axis graphbuilder={ this.state.data.Graph_builder_field } title="Columns" name="x_column" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.module } valueType={ this.state.x_column } columnLength="col-lg-4 col-md-4 col-sm-6"/>
                    		 </div>

                    		 <div className="row mt-1">
                    		 	<Axis graphbuilder={ this.state.data.Graph_builder_field } title="Values" name="valueType" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.module } valueType={ this.state.valueType } columnLength="col-lg-12 col-md-12 col-sm-12"/>
                    		 </div>

                    		 <div className="row mt-1">
	                    		 <div className="col-12">
    							  <label className="mx-2">
    							    <input type="radio" value="sum" 
    							                  checked={this.state.groupType === 'sum'} 
    							                  onChange={this.handleOptionChange} />
    							     Sum
    							  </label>

    							  <label className="mx-2">
    							    <input type="radio" value="count" 
    							                  checked={this.state.groupType === 'count'} 
    							                  onChange={this.handleOptionChange} />
    							     Count
    							  </label>
    							</div>
    						</div>

    						<hr/>

    						<div className="row mt-2">
                                	<h3 className="mx-4">{ this.state.table_name }</h3>
    						</div>
    						<div className="row mt-1">
    							<div className="col-12">
    								<FormulateReportData username={this.state.username} module_name={this.state.module} x_column={this.state.x_column} y_column={this.state.y_column} valueType={this.state.valueType} table_name={this.state.table_name} groupType={this.state.groupType} getData={ this.getData }/>
    							</div>
    						</div>

                      <button type="button" className="btn btn-primary btn-block" onClick={ this.handleSaveTableClick }>Save table</button>
						</div>
					</div>)
	}
}

export default TableBuilder

if (document.getElementById('table-builder')) {
	console.log("ID INTACT")
    ReactDOM.render(<TableBuilder />, document.getElementById('table-builder'));
}