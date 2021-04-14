import React from 'react';
import ReactDOM from "react-dom";
import {XYPlot, XAxis, YAxis, HorizontalGridLines, VerticalGridLines, ChartLabel, VerticalBarSeries as BarSeries, LineSeries} from 'react-vis';
import './../node_modules/react-vis/dist/style.css';

class LineGraph extends React.Component {
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
		console.log("Line graph data graph is ")
		console.log(this.props.data)
		return (<XYPlot
  					width={300}
  					height={300}>
  					<HorizontalGridLines />
  					<VerticalGridLines />
  					<LineSeries
    					data={this.props.data}
    					style={{ fill: 'none' }}
  					/>
  					<XAxis />
  					<YAxis />
				</XYPlot>)
			}
	}

export default LineGraph
