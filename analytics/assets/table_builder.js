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
			module: "all",
			moduleid: "",
			x_column: "",
			y_column: "",
			groupType: "sum",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			valueType: "",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)

		this.handleInputChanged = this.handleInputChanged.bind(this)
		this.handleAxisChanged = this.handleAxisChanged.bind(this)
		this.handleCheckboxInputChanged = this.handleCheckboxInputChanged.bind(this)
		this.handleGraphInputChanged = this.handleGraphInputChanged.bind(this)
		this.handleChartChange = this.handleChartChange.bind(this)
		this.handleOptionChange = this.handleOptionChange.bind(this)
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

	handleInputChanged(e, name){
		const value = e.target.value

		console.log("Setting module id to "+e.target.value)

		this.setState({
			[name]: value
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


	render(){
		// console.log("INSTANCE")
		// console.log(this.state.data)
		return (<div className="row">
						<div className="col-lg-7 col-md-8 col-sm-12">
							<div className="row mt-2">
								<div className="col-12">
									<label><h4>Table Name</h4></label>
									<input 
										type="text" 
										id="table_name" 
										placeholder="Enter name of the table" 
										name="table_name" 
										className="input-element" 
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
                    			<Axis graphbuilder={ this.state.data.Graph_builder_field } title="Rows" name="x_column" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.module } columnLength="col-lg-4 col-md-4 col-sm-6"/>

                    			<Axis graphbuilder={ this.state.data.Graph_builder_field } title="Columns" name="y_column" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.module } columnLength="col-lg-4 col-md-4 col-sm-6"/>
                    		 </div>

                    		 <div className="row mt-1">
                    		 	<Axis graphbuilder={ this.state.data.Graph_builder_field } title="Values" name="valueType" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.module } columnLength="col-lg-12 col-md-12 col-sm-12"/>
                    		 </div>

                    		 <div className="row mt-1">
	                    		 <div className="col-12">
    							  <label className="mx-2">
    							    <input type="radio" value="sum" 
    							                  checked={this.state.valueType === 'sum'} 
    							                  onChange={this.handleOptionChange} />
    							     Sum
    							  </label>

    							  <label className="mx-2">
    							    <input type="radio" value="count" 
    							                  checked={this.state.valueType === 'count'} 
    							                  onChange={this.handleOptionChange} />
    							     Count
    							  </label>
    							</div>
    						</div>

    						<hr/>

    						<div className="row mt-2">
    							<FormulateReportData module_name={this.state.module} x_column={this.state.x_column} y_column={this.state.y_column} valueType={this.state.valueType} groupType={this.state.groupType}/>
    						</div>

                      <button type="submit" className="btn btn-primary btn-block">Save table</button>
						</div>
					</div>)
	}
}

export default TableBuilder

if (document.getElementById('table-builder')) {
	console.log("ID INTACT")
    ReactDOM.render(<TableBuilder />, document.getElementById('table-builder'));
}