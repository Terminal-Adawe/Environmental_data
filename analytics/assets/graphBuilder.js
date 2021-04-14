import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

import Axis from './axis';
import GraphImage from './graphImage';



class GraphBuilder extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			module: "all",
			moduleid: 1,
			xaxis: "",
			yaxis: "",
			chartType: "Bar Chart",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)

		this.handleInputChanged = this.handleInputChanged.bind(this)
		this.handleAxisChanged = this.handleAxisChanged.bind(this)
		this.handleCheckboxInputChanged = this.handleCheckboxInputChanged.bind(this)
		this.handleGraphInputChanged = this.handleGraphInputChanged.bind(this)
		this.handleChartChange = this.handleChartChange.bind(this)
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

	handleInputChanged(e){
		const value = e.target.value

		console.log("Setting module id to "+e.target.value)

		this.setState({
			moduleid: value
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

		name === "x-axis" ?
		this.setState({
			xaxis: value
		})
		: 
		this.setState({
			yaxis: value
		})
	}

	handleChartChange(e){
		this.setState({
			chartType: e.target.value
		})
	}


	render(){
		// console.log("INSTANCE")
		// console.log(this.state.data)
		return (<div className="row">
						<div className="col-lg-7 col-md-8 col-sm-12">
							<div className="row mt-2">
								<label><h4>Graph Name</h4></label>
								<input 
									type="text" 
									id="graph_name" 
									placeholder="Enter name of the graph" 
									name="graph_name" 
									className="input-element" 
									 />
							</div>
							<div className="row mt-2">
                    			<div className="col-12">
								<label><h4>Select Graph Type</h4></label>
                    		 	<select id="chart" name="chart" defaultValue="" className="input-element" onChange={(e)=>this.handleChartChange(e)}>
										<option value=""></option>
							{
								this.state.data.Chart  ?
							
								this.state.data.Chart.map((chart,i)=>{
												return <option key={i} value={ chart.chart_name }>{ chart.chart_name }</option>

										
								})
								: ""
							}
								</select>
                    		  	</div>
                    		</div>

                    		<GraphImage chartType={ this.state.chartType } charts={ this.state.data.Chart }/>

							<div className="row mt-2">
								<div className="col-12">
									<label><h5>Select Module</h5></label>
									<select id="module" name="module" defaultValue="1" className="input-element" onChange={(e)=>this.handleInputChanged(e)}>
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
                    		 </div>

                    		<Axis graphbuilder={ this.state.data.Graph_builder_field } title="X-Axis" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.moduleid }/>

                    		<Axis graphbuilder={ this.state.data.Graph_builder_field } title="Y-Axis" handleAxisChanged={ this.handleAxisChanged } moduleid={ this.state.moduleid }/>

                    		<label className="form-check-label predictive_label">
                    		<h5>Predictive</h5>
                      	<input 
                      		type="checkbox" 
                      		className="form-check-input 
                      		current input-element" 
                      		name="predictive" 
                      		defaultValue="1" 
                      		onChange={(e)=>this.handleCheckboxInputChanged(e)}
                      		/>
                      </label>

                      <button type="submit" className="btn btn-primary btn-block">Submit</button>
						</div>
					</div>)
	}
}

export default GraphBuilder

if (document.getElementById('graph-builder')) {
	console.log("ID INTACT")
    ReactDOM.render(<GraphBuilder />, document.getElementById('graph-builder'));
}