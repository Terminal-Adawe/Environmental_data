import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";

import CustomTables from './custom_table';
import ReportGraphs from './reportGraphs';
import AddText from './AddText'
import Notes from './notes'


class ViewReport extends React.Component {
	constructor(){
		super()

		this.state={
			username: document.getElementById("username").value,
			data: [],
			module: "",
			report_id: "",
			report_name: "",
			notes: [],
			edit_mode: 0,
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			get_report_url: '/analytics/get-report/',
			save_report_structure: '/analytics/api/save_report_structure',
			save_notes_url: '/analytics/api/save_notes/'
			// baseUrl: "http://localhost:8002",
		}

		this.getReport = this.getReport.bind(this)
		this.textAreaChangeFunc = this.textAreaChangeFunc.bind(this)
		this.saveStructure = this.saveStructure.bind(this)
		this.restructure = this.restructure.bind(this)
		this.saveNote_api = this.saveNote_api.bind(this)
		this.saveStructure_api = this.saveStructure_api.bind(this)
		this.updateNotes = this.updateNotes.bind(this)
		this.edit_mode_switch = this.edit_mode_switch.bind(this)
	}

	componentDidMount(){
		const baseUrl = document.getElementById("baseUrl").value
		const report_id = document.getElementById("reportID").value
		const username = document.getElementById("username").value
		// const report_name = document.getElementById("reportName").value
		// const type = document.querySelector(".save_button_type").value

		this.setState({
			baseUrl: baseUrl,
			report_id: report_id,
			username: username
		},()=>{
			this.getReport(report_id)
		})
	}

	edit_mode_switch(){
		this.setState({
			edit_mode: !this.state.edit_mode
		})
	}


	getReport(report_id){
		const url = this.state.get_report_url

		axios.get(`${this.state.baseUrl}${url}`,
							{
							params: {
								id: report_id
							}
							},{
                headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                 },
            })
        	.then(response => {
        		console.log("The report response is ")
        		console.log(response.data)
          this.setState({
            data: response.data,
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}

	textAreaChangeFunc(e, position, positionid){
		console.log("Position is ")
		console.log(position)
		console.log(" + ")
		console.log(positionid)
		console.log(" + ")
		console.log(e.target.value)
		console.log(" + ")
		console.log(this.state.data)

		const jsonStructure = {"category": "note", "report_name": this.state.report_id, "the_id": position+positionid, "module_id": "custom"}

		const temp_id = position+positionid
		this.restructure(position, positionid, temp_id, e.target.value, jsonStructure)


	}

	updateNotes(data, action){
		let notes = this.state.notes

		if(action=="add"){
			notes.push(data)
		}

		this.setState({
			notes: notes
		})
	}

	restructure(position, positionid, temp_id, value, nStructure){

		// Get structure of report
		let structure = this.state.data

		// Create array to hold notes
		let note_s = []
		let note_m = this.state.notes

		// Initialize notes array with temp entries
		note_s = [temp_id, value, 0]

		console.log("Structure is ")
		console.log(structure)

		let calcPos = positionid

		if(position=="above"){
			calcPos = positionid-1
		}

		if(position=="below"){
			calcPos = positionid+1			
		}

		var exists = 0

		var note_exist = 0
		
		// Filter structure to find category that matches a note and ID is same as new payload
		structure.filter(struc=>(struc.the_id==nStructure.the_id) && (struc.category=="note")).map((struc,i)=>{
			exists = 1
			note_exist = 1

			struc.report_name = nStructure.report_name

			// Initialize single note array. 
			// ID of the note already stored in the structure.
			// 
			note_s = [struc.the_id, value, 0]
		})

		if(exists==0){
			structure.splice(positionid,0,nStructure)
			note_m.push(note_s)
		}

		if(note_exist==1){
			note_m.filter(note=>note[0]==temp_id).map((note,i)=>{
				note[1] = value
			})
		}

		this.setState({
			notes: note_m
		})
		
	}

	saveStructure(){
		const data = this.state.data
		let notes = this.state.notes
		const report_id = this.state.report_id

		this.setState({
			edit_mode: !this.state.edit_mode
		})

		console.log("I have data as")
		console.log(data)

		// Loop through current array
		// Check if the_id param is a string. Strings show it is newly inserted.
		data.filter(struct=>(typeof(struct.the_id)=="string" && 
			struct.the_id.indexOf("above") != -1) 
		|| (typeof(struct.the_id)=="string" 
			&& struct.the_id.indexOf("below") != -1)).map((struct,i)=>{
			console.log("each Structure is ")
			// str = struct.the_id
			console.log(struct)

			let action = "add"
			let note_id = "none"

			// Loop through notes array and compare with structure array
			// If structure array already has note ID, then update else insert new note
			notes.map((note,i)=>{
				if(note[1]==struct.the_id){
					action = "update"
					note_id = struct.the_id
				}
				

				// Get position from some skematics
				let position = note_id.split('above')
	
				try{
					position = position.split('below')
				} catch(err){
					console.log("Error enlisted is ")
					console.log(err)
				}

			console.log("Says to "+action)
			console.log(position)

			this.saveNote_api(note[1],action,note_id,report_id,position[1])

			})
			
			
		})

		
	}


	saveNote_api(note, action, note_id, report_id, position){
		let form_data = new FormData();

		const username = this.state.username
    
    	form_data.append('notes', note)
    	form_data.append('action', action)
    	form_data.append('note_id', note_id)
    	form_data.append('report_id', report_id)
    	form_data.append('username', username)


    	const baseUrl = this.state.baseUrl
    	const url = this.state.save_notes_url

    	console.log("username being sent is ")
    	console.log(username)

		axios.post(`${baseUrl}${url}`,form_data,{
                    headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                     enctype: 'multipart/form-data'
                    },
                })
                .then(response => {
                    console.log("report structure save response is ")
                    console.log(response)
                    // this.props.loader(false)

                    if(response.status == "201"){
                        // Successful upload
                        console.log("Note ID is ")
                        console.log(response.data.id)
                        this.saveStructure_api("note", response.data.id, note_id, reportid, "custom", action, position)
                    } else {
                        // Failed upload
                    }

                })
                .catch(error => {
                    this.props.loader(false)
                    console.log(error)
                    document.getElementById('error-message').innerHTML = error
                    setTimeout(function(){
                        document.getElementById('error-message').innerHTML = ""
                    },10000)
                // console.log("an error occurred!!")
                })
	}


	saveStructure_api(category, the_id, old_note_id, reportid, module_id, action, position){
		let form_data = new FormData();
    
    	form_data.append('category', category)
    	form_data.append('the_id', the_id)
    	form_data.append('reportid', reportid)
    	form_data.append('module_id', module_id)
    	form_data.append('action', action)
    	form_data.append('position', position)
    	form_data.append('username', this.state.username)


    	// Get structure
    	let structure = this.state.data

    	// replace note ID with new inserted note ID
    	structure.filter(struct=>struct.the_id==old_note_id).map((struct,i)=>{
    		struct.the_id = the_id
    	})

    	this.setState({
    		data: structure
    	},()=>{
    		console.log("Structure is now ")
    		console.log(this.state.data)

    		form_data.append("full_structure",this.state.da)
    	})


		axios.post(`${baseUrl}${save_report_structure}`,form_data,{
                    headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                     enctype: 'multipart/form-data'
                    },
                })
                .then(response => {
                    console.log("report structure save response is ")
                    console.log(response)
                    // this.props.loader(false)

                    if(response.status == "201"){
                        // Successful upload
                    } else {
                        // Failed upload
                    }

                })
                .catch(error => {
                    this.props.loader(false)
                    console.log(error)
                    document.getElementById('error-message').innerHTML = error
                    setTimeout(function(){
                        document.getElementById('error-message').innerHTML = ""
                    },10000)
                // console.log("an error occurred!!")
                })
	}


	render(){
		return (
				<div className="container-fluid">
					{
						this.state.data.map((structure,i)=>{
							console.log("Going through this structure...")
							console.log(structure)
							if(structure.category=="table" && structure.module_id=="custom"){
								return <React.Fragment key={i}>
												{
													this.state.edit_mode ?
													<AddText position="above" positionid={i} textAreaChangeFunc={this.textAreaChangeFunc}/>
													: ''
												}
												<CustomTables table_id={ structure.the_id }/>
												{
													this.state.edit_mode ?
													<AddText position="below" positionid={i} textAreaChangeFunc={this.textAreaChangeFunc}/>
													: ''
												}			
												<hr/>
											</React.Fragment>
							} else if (structure.category=="graph" && structure.module_id == "custom"){
								return <React.Fragment key={i}>
												{
													this.state.edit_mode ?
													<AddText position="above" positionid={i} textAreaChangeFunc={this.textAreaChangeFunc}/>
													: ''
												}
												<ReportGraphs  graphid={structure.the_id} module="all" />
												{
													this.state.edit_mode ?
													<AddText position="below" positionid={i} textAreaChangeFunc={this.textAreaChangeFunc}/>
													: ''
												}	
												<hr/>
											</React.Fragment>
							} else if (structure.category=="note" && structure.module_id == "custom"){
								console.log("matched note")
								return <React.Fragment key={i}>
												{
													this.state.edit_mode ?
													<AddText position="above" positionid={i} textAreaChangeFunc={this.textAreaChangeFunc}/>
													: ''
												}
												<Notes  notes_id={structure.the_id} module="all" updateNotes={ this.updateNotes }/>
												{
													this.state.edit_mode ?
													<AddText position="below" positionid={i} textAreaChangeFunc={this.textAreaChangeFunc}/>
													: ''
												}	
												<hr/>
											</React.Fragment>
							} else {
								return <div key={i}></div>
							}
						})
					}
					<div className="row">
					{
						this.state.edit_mode ?
						<button className="btn btn-secondary mx-4" type="button" onClick={ this.saveStructure }>Save Report</button>
						:
						<button className="btn btn-secondary mx-4" type="button" onClick={ this.edit_mode_switch }>Edit</button>
					}
						
					</div>
				</div>
			)
	}
}

export default ViewReport


if (document.getElementById('view_report')) {
		 ReactDOM.render(<ViewReport />, document.getElementById('view_report'));
    
}