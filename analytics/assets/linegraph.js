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
		console.log("All data graph is ")
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
  					<ChartLabel
    					text="Y Axis"
    					className="alt-y-label"
    					includeMargin={true}
    					xPercent={0.05}
    					yPercent={0.10}
    					style={{
    					  transform: 'rotate(-90)',
    					  textAnchor: 'end'
    					}}
    				/>
  					<XAxis />
  					<YAxis />
				</XYPlot>)
			}
	}

export default LineGraph
