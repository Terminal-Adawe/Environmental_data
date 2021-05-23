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
			username: "",
			data: [],
			notifications: [],
			tasks: [],
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
		this.formatDate = this.formatDate.bind(this)

	}

	componentDidMount(){

		const baseUrl = document.getElementById("baseUrl").value
		const username = document.querySelector(".username").value

		console.log("notifications user id is ")
		console.log(username)

		this.setState({
			baseUrl: baseUrl,
			username: username
		},()=>{
			this.getDetails()
		})
	}

	getDetails(){
		axios.get(`${this.state.baseUrl}/analytics/get-notifications/`)
        	.then(response => {
        		console.log("Notification response is ")
        		console.log(response.data)
        		console.log("count is ")
        		console.log(response.data.Notifications.length)

        		var tasks = response.data.Tasks.filter(task=>task.task_for==this.state.username)
        		console.log("modified tasks are ")
        		console.log(tasks)
        		console.log(" v ")
        		console.log(this.state.username)

          this.setState({
            notifications: response.data.Notifications,
            tasks: tasks

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
								<span className="badge">{ this.state.tasks.length }</span>
							</a>
			
							<div className="dropdown-menu notification-menu large">
								<div className="notification-title">
									<span className="pull-right label label-default">{ this.state.tasks.length }</span>
									Tasks
								</div>
			
								<div className="content">
									<ul>
										{
											this.state.tasks.map((task,i)=>{
												return <li key={ i }>
													<a href="#" className="btn btn-default">
														<p className="clearfix mb-xs">
															<span className="custom-message pull-left text-report-notif">{ task.task }</span>
															<span className="message pull-right text-dark">{ this.formatDate(task.start_time) } to { this.formatDate(task.end_time) }</span>
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