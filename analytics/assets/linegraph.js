import React from 'react';
import ReactDOM from "react-dom";
import {XYPlot, XAxis, YAxis, 
  HorizontalGridLines, VerticalGridLines, ChartLabel, 
  VerticalBarSeries as BarSeries, LineSeries, FlexibleXYPlot,
  FlexibleWidthXYPlot, Crosshair} from 'react-vis';

class LineGraph extends React.Component {
	constructor(){
		super()

    this.state={
      showHint: false,
      value: "",
      crosshairValues: []
    }

    this.showHint = this.showHint.bind(this)
    this._onMouseLeave = this._onMouseLeave.bind(this)
    this._onNearestX = this._onNearestX.bind(this)
	}


  showHint(boolval,value){
    this.setState({
      showHint: boolval,
      value: value,
    })
  }

  _onMouseLeave () {
      this.setState({crosshairValues: []});
    };

  _onNearestX (value, {index}) {
      this.setState({crosshairValues: this.props.data.map(d => d[index])});
    };




	render(){
		console.log("Line graph data graph is ")
		console.log(this.props.data)
		return (<FlexibleWidthXYPlot
  					height={300}
            onMouseLeave={this._onMouseLeave}>
  					<HorizontalGridLines />
  					<VerticalGridLines />
  					<LineSeries
    					data={this.props.data}
    					style={{ fill: 'none' }}
              onNearestX={this._onNearestX}
  					/>
  					<XAxis />
  					<YAxis />
            <Crosshair
              values={this.state.crosshairValues}
            />
				</FlexibleWidthXYPlot>)
			}
	}

export default LineGraph
