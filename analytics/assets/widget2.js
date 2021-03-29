import React from 'react';
import ReactDOM from "react-dom";



class Widgets_b extends React.Component {
	constructor(){
		super()
	}


	render(){
		return (<React.Fragment>{this.props.compliance ? this.props.compliance.filter(value=>value.parameter==this.props.parameter).map((value,i)=>{
				return <section className="panel" key={i}>
											<div className="panel-body bg-secondary">
												<div className="widget-summary">
													<div className="widget-summary-col widget-summary-col-icon">
														<div className="summary-icon">
															<i className="fa fa-life-ring"></i>
														</div>
													</div>
													<div className="widget-summary-col">
														<div className="summary">
															<h4 className="title">{ this.props.compliance ? value.parameter : "none" }</h4>
															<div className="info">
																<strong className="amount">{ this.props.compliance ? value.value : "none" }</strong>
															</div>
														</div>
														<div className="summary-footer">
															<a className="text-uppercase">S</a>
														</div>
													</div>
												</div>
											</div>
										</section>
			}) : ''
		}</React.Fragment>)
	}
}

export default Widgets_b
