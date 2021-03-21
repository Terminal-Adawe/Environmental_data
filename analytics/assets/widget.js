import React from 'react';
import ReactDOM from "react-dom";



class Widgets extends React.Component {
	constructor(){
		super()
	}


	render(){

		console.log("Gotten to widget ")
		console.log(this.props.compliance ? this.props.compliance : 'none')
		return (<div className="widget-summary widget-summary-xlg">
											<div className="widget-summary-col widget-summary-col-icon">
												<div className="summary-icon bg-primary">
													<i className="fa fa-life-ring"></i>
												</div>
											</div>
											<div className="widget-summary-col">
												<div className="summary">
													<h4 className="title">Support Questions</h4>
													<div className="info">
														<strong className="amount">{ this.props.compliance ? this.props.compliance.parameter : "none" }</strong>
														<span className="text-primary">(14 unread)</span>
													</div>
												</div>
												<div className="summary-footer">
													<a className="text-muted text-uppercase">(view all)</a>
												</div>
											</div>
										</div>)
	}
}

export default Widgets
