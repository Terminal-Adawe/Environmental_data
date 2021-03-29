import React from 'react';
import ReactDOM from "react-dom";
import {XYPlot, XAxis, YAxis, HorizontalGridLines, VerticalGridLines, VerticalBarSeries as BarSeries, LineSeries} from 'react-vis';

class BarGraph extends React.Component {
	constructor(){
		super()

    this.state={
      showHint: false,
      value: ""
    }

    this.showHint = this.showHint.bind(this)
	}


  showHint(boolval,value){
    this.setState({
      showHint: boolval,
      value: value,
    })
  }



	render(){
		return (<XYPlot
  width={300}
  height={300}>
  <HorizontalGridLines />
  <VerticalGridLines />
  <BarSeries
  	color="#85c1e9"
    data={this.props.data}
    onValueMouseOver={(datapoint, event)=>{
    // does something on click
    // you can access the value of the event
    // console.log("datapoint is ")
    // console.log(datapoint.y)
    // console.log(" and event is ")
    // console.log(this.state.showHint)

    this.showHint(true, datapoint.y)
    
  }}
  onValueMouseOut={(datapoint, event)=>{
    // does something on click
    // you can access the value of the event
    console.log(" mouse out is  ")
    console.log(this.state.showHint)
    this.showHint(false, datapoint.y)
  }}
  animation/>
  <XAxis />
  <YAxis />
</XYPlot>)
	}
}

export default BarGraph
