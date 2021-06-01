import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";


class Axis extends React.Component {
	constructor(){
		super()
	}




	render(){
		let name = this.props.name
		let axis = this.props.name


		return (<div className={ this.props.columnLength }>
								<label><h5>Select { this.props.title }</h5></label>
                    		 
							{
								this.props.graphbuilder  ?
								<select id={ name } name={ name } value={this.props.valueType} className="input-element" onChange={(e)=>this.props.handleAxisChanged(e,axis)}>
										{ this.props.title === "Y-Axis" ? <option value="sequence">Sequence</option> : <option value=""></option> }
										{
								this.props.graphbuilder.filter(field=>field.module==this.props.moduleid).map((field,i)=>{
											let columns = field.column_fields.split(",")
											return <React.Fragment key={ i }>
											{
												columns.map((column,r)=>{
													return <option key={r} value={ column }>{ column }</option>
												})
											}
												</React.Fragment>
								})
										}
								{ this.props.title === "X-Axis" ? <option value="sequence">Sequence</option> : "" }
										</select>
								: ""
							}
                    		  	</div>)
	}
}

export default Axis