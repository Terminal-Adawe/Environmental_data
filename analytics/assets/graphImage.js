import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";


class GraphImage extends React.Component {
	constructor(){
		super()
	}




	render(){

		return (<div className="row mt-2">
                    	{
                    		this.props.charts ?
                    		this.props.charts.filter(chart=>chart.chart_name==this.props.chartType).map((chart,i)=>{
                    			console.log("url is ")
                    			console.log(chart.image)
                    			return <div className="mx-auto chart-div" key={i} >
                    					<img src={chart.image} width="100%"  className="mx-auto"/>
                    				</div>
                    		})	
                    		: ""
                    	}
                </div>)
	}
}

export default GraphImage