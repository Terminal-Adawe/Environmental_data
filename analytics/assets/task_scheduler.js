import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

import GraphImage from './graphImage';



function TextInput(props){
	return <input type="text" name={ props.name } defaultValue={ props.task } onChange={(ev)=>props.handleInputChange(ev,"task")} required />
}


class Task_scheduler extends React.Component {
	constructor(){
		super()

		this.state={
			username: "",
			form: {
				task: "",
				descriptiioin: "",
				start_time: "",
				end_time: "",
				task_for: ""
			},
			users: [],
			taskType: "",
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
		}

		this.getDetails = this.getDetails.bind(this)
		this.addTask = this.addTask.bind(this)
		this.formatDate = this.formatDate.bind(this)
		this.handleTaskForChange = this.handleTaskForChange.bind(this)
		this.handleInputChange = this.handleInputChange.bind(this)

	}

	componentDidMount(){

		const baseUrl = document.getElementById("baseUrl").value
		const userid = document.getElementById("username").value
		const task_type = document.getElementById("task_type").value

		// console.log("user id is ")
		// console.log(task_type)

		this.setState({
			baseUrl: baseUrl,
			username: document.getElementById("username").value
		},()=>{
			this.getDetails()
		})
	}

	getDetails(){
		axios.get(`${this.state.baseUrl}/analytics/get-users/`)
        	.then(response => {
        		// console.log("Users response is ")
        		// console.log(response.data.User)
        		// console.log("count is ")
        		// console.log(response.data.User.length)

        		var taskType = "self"

        		response.data.User.map((user,i)=>{
        			// console.log("username is ")
        			// console.log(user.username)
        			// console.log("and state username is ")
        			// console.log(this.state.username)
        			if(user.username == this.state.username && user.is_staff==1){
        				taskType = "other"
        			}
        		})

          this.setState({
            users: response.data.User,
            taskType: taskType,
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}

	addTask(){
		console.log("add task")
		axios.get(`${this.state.baseUrl}/analytics/api/add-task/`,)
        	.then(response => {
        		// console.log("Add task response is ")
        		// console.log(response.data.User)
        		// console.log("count is ")
        		// console.log(response.data.User.length)
          this.setState({
            users: response.data.User,
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}

	handleTaskForChange(ev){
		console.log(e.target.value)

		var form = this.state.form

		form.task_for = e.target.value

		this.setState({
            form: form,
          })
	}

	handleInputChange(ev,inputName){
		console.log("about to print...")
		console.log(ev.target.value)

		var form = this.state.form

		form.[inputName] = ev.target.value

		this.setState({
            form: form,
          },()=>{
          	console.log("form is ")
          	console.log(this.state.form)
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
		// console.log("task type")
		// console.log(this.state.taskType)
		return (<div className="container-fluid">
            <div className="row">
            <label>Task</label>
              <TextInput task={ this.state.form.task } handleInputChange={ this.handleInputChange } name="task" />
            </div>
            	<div className="row">
            		<label>Task For:</label>
            		<select name="task_for" onChange={this.handleTaskForChange} defaultValue={ this.state.form.start_time }>
            			<option value="self">Self</option>
            			{
            				this.state.taskType=="other" ? 
            					this.state.users.map((user,i)=>{
            						if(user.username != this.state.username){
            							return <option key={i} value={ user.username }>{ user.username }</option>
            						}
            					})
            				: ""
            			}
                      </select>
                 </div>
            <div className="row">
              <label>Add Description</label>
              <textarea name="description" onChange={(ev)=>this.handleInputChange(ev,"description")}/>
            </div>
            <div className="row">
              <span className="mx-auto">Select a date range</span>
            </div>
            <div className="row">
              <div className="col-lg-6 col-md-6 col-sm-12">
              	<label>Start time</label>
                <input type="date" name="start_time" defaultValue={ this.state.form.start_time } onChange={ (ev)=>this.handleInputChange(ev,"start_time") }/>
              </div>
              <div className="col-lg-6 col-md-6 col-sm-12">
              	<label>End time</label>
                <input type="date" name="end_time" defaultValue={ this.state.form.end_time } onChange={ (ev)=>this.handleInputChange(ev,"end_time") } />
              </div>
            </div>
            <div className="row mt-4">
              <div className="col-lg-4 col-sm-6">
                <button className="btn btn-info" type="submit" onClick={ this.addTask }>Schedule Task</button>
              </div>
              <div className="col-lg-4 col-sm-6">
              </div>
            </div>
        </div>)
	}
}

export default Task_scheduler

if (document.getElementById('task_scheduler')) {
    ReactDOM.render(<Task_scheduler />, document.getElementById('task_scheduler'));
}