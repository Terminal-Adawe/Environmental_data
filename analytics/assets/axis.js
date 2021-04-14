import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";


class Axis extends React.Component {
	constructor(){
		super()
	}




	render(){
		let name = ""
		let axis = ""
		this.props.title === "Y-Axis" ? 
		name="y-axis"
		: 
		name="x-axis"

		return (<div className="row mt-2">
                    			<div className="col-12">
								<label><h5>Select { this.props.title }</h5></label>
                    		 
							{
								this.props.graphbuilder  ?
							
								this.props.graphbuilder.filter(field=>field.module==this.props.moduleid).map((field,i)=>{
									let columns = field.column_fields.split(",")
									return <select key={ i } id={ name } name={ name } defaultValue="" className="input-element" onChange={(e)=>this.props.handleAxisChanged(e,axis)}>
										{ this.props.title === "Y-Axis" ? <option value="sequence">Sequence</option> : "" }
										{
											columns.map((column,r)=>{
												return <option key={r} value={ column }>{ column }</option>
											})
										}
										{ this.props.title === "X-Axis" ? <option value="sequence">Sequence</option> : "" }
										</select>
								})
								: ""
							}
                    		  	</div>
                    		</div>)
	}
}

export default Axis