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
    this._onNearestXY = this._onNearestXY.bind(this)
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

  _onNearestXY (value, {event, innerX, innerY, index}) {
      // console.log("value is "+value.x+" and inner x is "+innerX+" and inner Y is "+innerY+" and index is "+index)
      // console.log(value)
      this.setState({crosshairValues: [value.x,value.y]});
    };




	render(){
		// console.log("Line graph data graph is ")
		// console.log(this.props.data)

    const crosshairvalues_all = this.state.crosshairValues

    console.log(crosshairvalues_all)

		return (<FlexibleWidthXYPlot
  					height={289}
            onMouseLeave={this._onMouseLeave}>
  					<HorizontalGridLines />
  					<VerticalGridLines />
  					<LineSeries
    					data={this.props.data}
    					style={{ fill: 'none' }}
              onNearestXY={this._onNearestXY}
  					/>
  					<XAxis />
  					<YAxis />
            <Crosshair
              values={this.state.crosshairValues}
            >
              <div style={{background: 'black'}}>
                <h3>Values of crosshair:</h3>
                <p>Series 1: {crosshairvalues_all[0]}</p>
                <p>Series 2: {crosshairvalues_all[1]}</p>
              </div>
            </Crosshair>
				</FlexibleWidthXYPlot>)
			}
	}

export default LineGraph
