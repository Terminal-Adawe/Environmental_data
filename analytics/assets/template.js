import React from 'react';
import ReactDOM from "react-dom";
import {XYPlot, XAxis, YAxis, HorizontalGridLines, VerticalBarSeries as BarSeries, LineSeries} from 'react-vis';
import Widgets from './widget';

function ColumnMaker(props){
	let data = []
	console.log("Props are ")
	console.log(props.data.Storage_facility)
	console.log(props)

	const storage_facility_data = props.data.Storage_facility

	storage_facility_data ?
	storage_facility_data.map((val, i)=>{
		console.log("Value given is "+val.current_capacity)
				data = [...data, {'x': i, y: val.current_capacity}]
			})
		
		: ""


									
										return (<div className="col-lg-6 col-sm-12">
											<XYPlot
  width={300}
  height={300}>
  <HorizontalGridLines />
  <BarSeries
  	color="red"
    data={data}
    onValueMouseOver={(datapoint, event)=>{
    // does something on click
    // you can access the value of the event
    // console.log("datapoint is ")
    // console.log(datapoint)
    // console.log(" and event is ")
    // console.log(event)
    
  }}
  animation
    />
  <BarSeries
  	color="blue"
    data={data}
    onValueMouseOver={(datapoint, event)=>{
    // does something on click
    // you can access the value of the event
    // console.log("datapoint is ")
    // console.log(datapoint)
    // console.log(" and event is ")
    // console.log(event)
    
  }}/>
  <BarSeries
  	color="green"
    data={data}
    onValueMouseOver={(datapoint, event)=>{
    // does something on click
    // you can access the value of the event
    // console.log("datapoint is ")
    // console.log(datapoint)
    // console.log(" and event is ")
    // console.log(event)
    
  }}
  animation/>
  <XAxis />
  <YAxis />
</XYPlot>
</div>)
									
								
	}

class Template extends React.Component {
	constructor(){
		super()
	}




	render(){
		return (<div className="row">
					<div className="col-12">
						<div className="row">
								<Widgets compliance={ this.props.data.ComplianceValue } />
								<ColumnMaker data={ this.props.data}/>
							
						</div>
					</div>
  			</div>)
	}
}

export default Template