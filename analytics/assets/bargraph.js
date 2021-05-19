import React from 'react';
import ReactDOM from "react-dom";
import {XYPlot, XAxis, YAxis, 
  HorizontalGridLines, VerticalGridLines, VerticalBarSeries, 
  LineSeries, LabelSeries, FlexibleXYPlot,
  FlexibleWidthXYPlot,} from 'react-vis';

const greenData = [{x: 'A', y: 10}, {x: 'B', y: 5}, {x: 'C', y: 15}];

const blueData = [{x: 'A', y: 12}, {x: 'B', y: 2}, {x: 'C', y: 11}];

const labelData = greenData.map((d, idx) => ({
  x: d.x,
  y: Math.max(greenData[idx].y, blueData[idx].y)
}));

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



	render() {
    const {useCanvas} = this.state;

    const BarSeries =  VerticalBarSeries;
    return (
      <div>
        <FlexibleWidthXYPlot xType="ordinal" height={300} xDistance={100}>
          <VerticalGridLines />
          <HorizontalGridLines />
          <XAxis />
          <YAxis />
          <BarSeries data={this.props.data} animation/>
        </FlexibleWidthXYPlot>
      </div>
    );
  }

}

export default BarGraph
