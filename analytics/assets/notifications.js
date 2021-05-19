import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

import Axis from './axis';
import GraphImage from './graphImage';



class Notifications extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
			notifications: [],
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
		this.formatDate = this.formatDate.bind(this)

	}

	componentDidMount(){

		const baseUrl = document.getElementById("baseUrl").value
		const userid = document.querySelector(".name")

		console.log("user id is ")
		console.log(userid)

		this.setState({
			baseUrl: baseUrl
		},()=>{
			this.getDetails()
		})
	}

	getDetails(){
		axios.get(`${this.state.baseUrl}/analytics/get-notifications/`)
        	.then(response => {
        		console.log("Notification response is ")
        		console.log(response.data.Notifications)
        		console.log("count is ")
        		console.log(response.data.Notifications.length)
          this.setState({
            notifications: response.data.Notifications,
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}

	formatDate(date) {
    	var d = new Date(date),
    	    month = '' + (d.getMonth() + 1),
    	    day = '' + d.getDate(),
    	    year = d.getFullYear();
	
    	if (month.length < 2) 
    	    month = '0' + month;
    	if (day.length < 2) 
    	    day = '0' + day;
	
    	return [year, month, day].join('-');
	}	



	render(){
		// console.log("INSTANCE")
		// console.log(this.state.data)
		return (<ul className="notifications">
						<li>
							<a href="#" className="dropdown-toggle notification-icon" data-toggle="dropdown">
								<i className="fa fa-tasks"></i>
								<span className="badge">0</span>
							</a>
			
							<div className="dropdown-menu notification-menu large">
								<div className="notification-title">
									<span className="pull-right label label-default">0</span>
									Tasks
								</div>
			
								<div className="content">
									<ul>
									</ul>
								</div>
							</div>
						</li>

						<li>
							<a href="#" className="dropdown-toggle notification-icon" data-toggle="dropdown">
								<i className="fa fa-envelope"></i>
								<span className="badge">0</span>
							</a>
			
							<div className="dropdown-menu notification-menu">
								<div className="notification-title">
									<span className="pull-right label label-default">0</span>
									Messages
								</div>
			
								<div className="content">
									<ul>
									</ul>
			
									<hr />
			
									<div className="text-right">
										<a href="#" className="view-more">View All</a>
									</div>
								</div>
							</div>
						</li>
						
						<li>
							<a href="#" className="dropdown-toggle notification-icon" data-toggle="dropdown">
								<i className="fa fa-bell"></i>
								<span className="badge">{ this.state.notifications.length }</span>
							</a>
			
							<div className="dropdown-menu notification-menu">
								<div className="notification-title">
									<span className="pull-right label label-default">{ this.state.notifications.length }</span>
									Alerts
								</div>
			
								<div className="content">
									<ul>
									{
										this.state.notifications.map((notification,i)=>{
											var url = `${this.state.baseUrl}/analytics/view_report/${notification.module}/${notification.report}/`
											return <li key={ i }>
													<a href={url} className="btn btn-default">
														<p className="clearfix mb-xs">
															<span className="custom-message pull-left text-report-notif">{ notification.message }</span>
															<span className="message pull-right text-dark">{ this.formatDate(notification.created_at) }</span>
														</p>
														{/*
														<div className="progress progress-xs light">
															<div className="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style={{width: '60%'}}></div>
														</div>
														*/}
													 </a>
													</li>
										})
									}
									</ul>
			
									<hr />
			
									<div className="text-right">
										<a href="#" className="view-more">View All</a>
									</div>
								</div>
							</div>
						</li>
				</ul>)
	}
}

export default Notifications

if (document.getElementById('notifications')) {
	console.log("ID INTACT")
    ReactDOM.render(<Notifications />, document.getElementById('notifications'));
}