import React from 'react';
import ReactDOM from 'react-dom';
import AddButton from './addButton';
// import Projects from './projects';
// import Duties from './duties';
// import Entries from './entries';

import axios from "axios";
import cookie from "react-cookies";


import { CountryDropdown, RegionDropdown, CountryRegionData } from 'react-country-region-selector';


function header(props){
		return <div className="card-header">
            		<h2>Professional Experience</h2>
            		<p>Tell us about your recent jobs</p>
            	</div>
	}

function Inputs(props){
		if(props.tag.inputtype=="text"){
			return <TextInput tag={props.tag} handleInputChanged={ props.handleInputChanged } form={ props.form }/>
		} else if (props.tag.inputtype=='date'){
			return <DateInput tag={props.tag} handleInputChanged={ props.handleInputChanged } form={ props.form } />
		} else if (props.tag.inputtype=='dropdown'){
			return <DropdownInput tag={props.tag} handleInputChanged={ props.handleInputChanged } certifications={ props.certifications } form={ props.form } />
		} else if (props.tag.inputtype=='country-dropdown'){
			return <CountryDropdownInput tag={props.tag} countrydropdownChange={ props.countrydropdownChange } country={ props.country } region={ props.region } form={ props.form }/>
		} else if (props.tag.inputtype=='checkbox'){
			return <CheckBox tag={props.tag} handleInputChanged={ props.handleInputChanged } form={ props.form }/>
		} else if (props.tag.inputtype=='' || props.tag.inputtype == "textarea"){
			console.log("Nothing to render..")
			return <></>
		}
	}

function Label(props){
		return <label htmlFor={props.tag.name}>{props.tag.label}</label>
	}

function FormFieldTemplate(props){
		// console.log("length of array is "+props.tag.length)
		// console.log(props.tag)

		let columnNo = 'col-12';

		switch(props.tag.length){
			case 1:
				columnNo = 'col-12'
				break
			case 2:
				columnNo = 'col-6'
				break
			case 3:
				columnNo = 'col-4'
				break
			default:
				columnNo = 'col-12'
				break;
		}

		return 	<div className="form-group">
                      <div className="row">
                        	{
                          		props.tag.map((formField,i)=>{
                          			return <React.Fragment key={ i }> 
                          			{
                          				formField.map((formFieldz,r)=>{
										return <div key={r} className={columnNo}>
											{ formFieldz.showlabel==1 ? <Label tag={ formFieldz } /> : <Label tag=""/> }
											<Inputs tag={ formFieldz } 
												handleInputChanged={ props.handleInputChanged } 
												country={ props.country } 
												region={ props.region }
												countrydropdownChange={ props.countrydropdownChange }
												certifications={ props.certifications }
												form={ props.form }
												/></div>
                          			})
                          			}
                          			</React.Fragment>
                          			
                          		})
                        	}
                      </div>
            	</div>
	}


function TextInput(props){
		return  <input 
					type="text" 
					id="company" 
					placeholder={props.tag.placeholder} 
					name={props.tag.name} 
					defaultValue={ props.form.[props.tag.name] }
					className="input-element" 
					onChange={(e)=>props.handleInputChanged(e)}
					required />

	}

function DateInput(props){
		return  <input type="date" 
					id={props.tag.name} 
					placeholder={props.tag.placeholder} 
					name={props.tag.name} 
					defaultValue={ props.form.[props.tag.name] }
					className="input-element" 
					onChange={(e)=>props.handleInputChanged(e)}
					/>
	}

function DropdownInput(props){
		console.log("props are ")
		console.log(props.certifications)

		return <select id={props.tag.name} name={props.tag.name} defaultValue={ props.form.[props.tag.name] } className="input-element" onChange={(e)=>props.handleInputChanged(e)}>
					{

						props.tag.options.map((option,i)=>{
							return <option key={i} value={ option[1] }>{ option[0] }</option>
						})
					}
                      </select>
	}

function CountryDropdownInput(props){
		return <div>
        		<CountryDropdown
          			value={props.country}
          			name={props.tag.name}
          			onChange={(val) => props.countrydropdownChange(val)} />
      			</div>
	}


function CheckBox(props){
		return <label className="form-check-label current_label" style={{paddingLeft: "20px"}}>
                      	<input 
                      		type="checkbox" 
                      		className="form-check-input 
                      		current input-element" 
                      		name="current" 
                      		defaultValue={ props.form.[props.tag.name] } 
                      		onChange={(e)=>props.handleInputChanged(e)}
                      		/>
                      		{props.tag.label} 
                      </label>
	}

class Form extends React.Component {
	constructor(){
		super()

		this.state = {
			csrfField: "",
			tags: [],
			formtype: document.getElementById("form_type").value,
			name: "",
			value: "",
			country: '', 
			region: '',
			form: {
				username: document.getElementById("username").value,
			},
			url: '',
			trigger: true,
			hiddencheck: '',
			certifications: [{ certification: 'none' }],
		}

		this.Grease_and_hydocarbon_spillageTags = this.Grease_and_hydocarbon_spillageTags.bind(this)
		this.storage_facilitiesTags = this.storage_facilitiesTags.bind(this)
		this.Waste_ManagementTags = this.Waste_ManagementTags.bind(this)
		this.IncenerationTags = this.IncenerationTags.bind(this)
		this.Liquid_waste_oilTags = this.Liquid_waste_oilTags.bind(this)


		this.handleInputChanged = this.handleInputChanged.bind(this)
		this.countrydropdownChange = this.countrydropdownChange.bind(this)
		this.updateEntries = this.updateEntries.bind(this)
		this.submitForm = this.submitForm.bind(this)
		this.getDetails = this.getDetails.bind(this)
		this.getCookie = this.getCookie.bind(this)

		this.tagDeclaration = this.tagDeclaration.bind(this)

		this.formRef = React.createRef();
	}

	componentDidMount(){
		console.log("componet mounted")
		if (this.state.formtype=="storage"){
			console.log("Storage chosen")
			this.storage_facilitiesTags()
		} else if (this.state.formtype=="Grease_and_hydocarbon_spillage"){
			console.log("Grease_and_hydocarbon_spillage chosen")
			this.Grease_and_hydocarbon_spillageTags()
		} else if (this.state.formtype=="Waste_Management"){
			console.log("Waste_Management chosen")
			this.Waste_ManagementTags()
		} else if (this.state.formtype=="Inceneration"){
			console.log("Inceneration chosen")
			this.IncenerationTags()
		} else if (this.state.formtype=="Liquid_waste_oil"){
			console.log("Liquid_waste_oil chosen")
			this.Liquid_waste_oilTags()
		} else if (this.state.formtype=="Health_and_hygiene_awareness"){
			console.log("Health_and_hygiene_awareness chosen")
			this.storage_facilitiesTags()
		} else if (this.state.formtype=="Energy_management"){
			console.log("Energy_management chosen")
			this.storage_facilitiesTags()
		} else if (this.state.formtype=="Complaints_register"){
			console.log("Complaints_register chosen")
			this.storage_facilitiesTags()
		} else if (this.state.formtype=="Slope_stabilization_and_surface_water_retention"){
			console.log("Slope_stabilization_and_surface_water_retention chosen")
			this.storage_facilitiesTags()
		} else if (this.state.formtype=="Safety_training"){
			console.log("Safety_training chosen")
			this.storage_facilitiesTags()
		} else if (this.state.formtype=="Safety_permission_system"){
			console.log("Safety_permission_system chosen")
			this.storage_facilitiesTags()
		}

		
	}

	componentDidUpdate(prevProps, prevState){
    	if(prevState.value != this.state.value){
    		console.log("reloading")
    		// console.log(this.state.name)
    		let form = this.state.form

    		if(this.state.name == "projects[]"){
    			// Form switch to trigger when a project id in the form matches the project id
    			// in the props
    			let switche = 0;
    			form.projects.map((project,i)=>{
    				// console.log("The project is ")
    				// console.log(project[0])
    				// console.log(" compared with ")
    				// console.log(this.state.value[0])
    				if(project[0]==this.state.value[0]){
    					project[1] = this.state.value[1]
    					switche = 1
    				}
    			})

    			if(switche==0){
    				// console.log("Projects are ")
    				// console.log(form.projects)
    				// console.log(this.state.value)
    				// console.log(form)
    				// console.log("Length of the project array is ")
    				// console.log(form.projects.length)
    				const projectArrayLength = form.projects.length
    				// form.projects[0] != "" ? form.projects = [...form.projects, form.projects[0]] : ""
    				// form.projects = [...form.projects, this.props.states.value]
  
    					form.projects = [...form.projects, this.state.value]

    				
    			}
    		} else if(this.state.name == "duties[]"){
    			// Form switch to trigger when a project id in the form matches the project id
    			// in the props
    			let switche = 0;
    			form.duties.map((duty,i)=>{
    				console.log("The duties is ")
    				console.log(duty)
    				// console.log(" compared with ")
    				// console.log(this.state.value[0])
    				if(duty[0]==this.state.value[0]){
    					duty[1] = this.state.value[1]
    					switche = 1
    				}
    			})

    			if(switche==0){
    				// console.log("Duties are ")
    				// console.log(form.duties)
    				// console.log(this.state.value)
    				// console.log(form)
    				// console.log("Length of the duty array is ")
    				// console.log(form.duties.length)
    				const dutyArrayLength = form.duties.length
    				// form.projects[0] != "" ? form.projects = [...form.projects, form.projects[0]] : ""
    				// form.projects = [...form.projects, this.props.states.value]
  
    					form.duties = [...form.duties, this.state.value]

    				
    			}
    		}
    		else {
    			form.[this.state.name] = this.state.value
    		}

    		console.log("Form is ")
    		console.log(form)


    		this.setState({
    			form: form
    		})

    		// console.log("updated form is ")
    		// console.log(this.state.form)
    	}
    }

    getCookie(name) {
    	var cookieValue = null;
    	if (document.cookie && document.cookie !== '') {
    	    var cookies = document.cookie.split(';');
    	    for (var i = 0; i < cookies.length; i++) {
    	        var cookie = jQuery.trim(cookies[i]);
    	        if (cookie.substring(0, name.length + 1) === (name + '=')) {
    	            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    	            break;
    	        }
    	    }
    	}
    		return cookieValue;
	}


    getDetails(){
		axios.get(`/api/get-details/`)
        	.then(response => {
        		console.log(response)
          this.setState({
            certifications: response.data.certifications,
          })
        })
        .catch(error => {
          // here catch error messages from laravel validator and show them 
          console.log(error)
     	})
	}

	tagDeclaration(tags, url){
		this.setState({
			tags: tags
		},()=>{
			let form = this.state.form


			tags.map((tag,i)=>{
				tag.formField.map((field,i)=>{
					// console.log("Field is ")
					// console.log(field[0].name)
					form.[field[0].name] = ""
				})
			})

			console.log("form after manipulation is ")
			console.log(form)

			this.setState({
				form: form,
				url: url
			})
		})
	}



	storage_facilitiesTags(){
		const tags = [
			{formField: [[{inputtype: 'text', name:'report_name',placeholder:'Report Name',label:'Name of Report',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'status_of_seepage_point',placeholder:'',label:'Status of Seepage Point',showlabel:1,options:[['Good','GD'],['Slightly Disturbed','SD'],['Blocked','BL']]}]]},
			{formField: [[{inputtype:'dropdown',name:'stability_of_dam_walls',placeholder:'',label:'Stability of Dam Walls',showlabel:1,options:[['Stable','STB'],['Signs of Erosion','SOE'],['Rehabilitated','RBT']]}]]},
			{formField: [[{inputtype: 'text', name:'holding_capacity',placeholder:'Enter Holding Capacity',label:'Holding Capacity',showlabel:1}]]},
			{formField: [[{inputtype:'text',name:'current_capacity',placeholder:'Enter Current Capacity',label:'Current Capacity',showlabel:1}]]},
			{formField: [[{inputtype:'text',name:'spillways_capacity',placeholder:'Enter Spillways Capacity',label:'Spillways Capacity',showlabel:1}]]},
			{formField: [[{inputtype:'text',name:'spillways_stability',placeholder:'Enter Spillways Stability',label:'Spillways Stability',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'signs_of_erosion_spillway_tip',placeholder:'Erosion Signs',label:'Signs of Erosion on Spillway Tip',showlabel:1,options:[['Yes','Y'],['No','N']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
		]

		const action_url = 'add/add-seepage/'

		this.tagDeclaration(tags, action_url)
	}

	Grease_and_hydocarbon_spillageTags(){
		const tags = [
			{formField: [[{inputtype: 'text', name:'report_name',placeholder:'Report Name',label:'Name of Report',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'storage_condition',placeholder:'',label:'Storage Condition',showlabel:1,options:[['Completely Impervious Surface','CIS'],['Partially Impervious','PI'],['Non Impervious','NI'],['Stored in Containment','SIC'],['Not Stored in Containment','NSIC']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			]

		const action_url = 'add/add-grease-and-hydrocarbon/'

		this.tagDeclaration(tags, action_url)
	}

	Waste_ManagementTags(){
		const tags = [
			{formField: [[{inputtype: 'text', name:'report_name',placeholder:'Report Name',label:'Name of Report',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'segregation_at_source_and_bins',placeholder:'',label:'Segregation at source and use of colored bins',showlabel:1,options:[['Effective','EF'],['Not Effective','NEF'],['Partially Effective','PEF'],['Sorted at Dump Site','SDS']]}]]},
			{formField: [[{inputtype: 'text', name:'glass_waste_source',placeholder:'Source',label:'Glass waste source',showlabel:1}],[{inputtype: 'text', name:'glass_waste_weight',placeholder:'Weight',label:'Glass waste weightage',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'plastic_waste_source',placeholder:'Source',label:'Plastic waste source',showlabel:1}],[{inputtype: 'text', name:'plastic_waste_weight',placeholder:'Weight',label:'Plastic waste weightage',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'metal_waste_source',placeholder:'Source',label:'Metal waste source',showlabel:1}],[{inputtype: 'text', name:'metal_waste_weight',placeholder:'Weight',label:'Metal waste weightage',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			]

		const action_url = 'add/add-waste-management/'

		this.tagDeclaration(tags, action_url)
	}

	IncenerationTags(){
		const tags = [
			{formField: [[{inputtype: 'text', name:'report_name',placeholder:'Report Name',label:'Name of Report',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'items_incenerated',placeholder:'Item name',label:'Item',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'quantity',placeholder:'Quantity',label:'Quantity',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'temperature',placeholder:'Temperature',label:'Temperature',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			]

		const action_url = 'add/add-inceneration/'

		this.tagDeclaration(tags, action_url)
	}

	Liquid_waste_oilTags(){
		const tags = [
			{formField: [[{inputtype: 'text', name:'report_name',placeholder:'Report Name',label:'Name of Report',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'discharge_point',placeholder:'Effluent Discharge Point',label:'Effluent Discharge Point',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'source',placeholder:'',label:'Source',showlabel:1,options:[['Maintenance Workshop','MW'],['Other Area','OA']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			]

		const action_url = 'add/add-liquid-waste-oil/'

		this.tagDeclaration(tags, action_url)
	}

	handleInputChanged(e, r, form){
		console.log("triggerd")
		// console.log(e.target.name)

		console.log(e.target.value)

		// console.log(e.target.type)

		// console.log(r)



		let value = e.target.type === 'checkbox' ? e.target.checked : e.target.value;

		if(e.target.name === "projects[]" || e.target.name === "duties[]"){

			value = [r,e.target.value]

		}

		this.setState({
			name: e.target.name,
			value: value
		})
	}

	countrydropdownChange(val){
		this.setState({
			country: val,
			name: "country",
			value: val
		})
	}

	updateEntries(form){
		// console.log("Triggered!")
		// console.log(form)
		this.setState({
			form: form,
			trigger: !this.state.trigger,
		},()=>{
			// console.log("renewed form is ")
			// console.log(this.state.form)
		})
	}

	submitForm(e,value){
		this.setState({
			hiddencheck: value
		},()=>{
			const node = this.formRef.current;

			console.log("submitting form")

			node.submit()
		})

		// node.dispatchEvent(new Event('submit'))
	}

	render(){

		let url = ""
		let action_url = ""
        if(this.state.formtype == "education"){
        	url = '/images/collegeboy.png'
        	action_url = '/saveeducation'
        } else if(this.state.formtype == "professional"){
        	url = '/images/worker.png'
        	action_url = '/saveprofesionaldetails'
        }

		return (<div className="row">
				<div className="col-lg-11 col-md-11 col-sm-12">
        <div className="card input-div-card">
          { this.header }

          <div className="card-body">
            <div className="container-fluid">
            	<div id="message">
            	</div>
              <div className="row">
                <div className="col-12">
                  <form action={ this.state.url } className="needs-validation" method='post' id="form" ref={this.formRef} noValidate>
                    <input type="hidden" name="_token" value={ this.state.csrfField } />
                    <input type="hidden" value={this.state.hiddencheck} id="hiddencheck" name='hiddencheck' />
                    	{
                    		// serious stuff here
                    		this.state.tags.map((tag,i)=>{
                    				 return <FormFieldTemplate key={i} 
                    				 	tag={ tag.formField } 
                    				 	handleInputChanged={ this.handleInputChanged } 
                    				 	countrydropdownChange={ this.countrydropdownChange } 
                    				 	country={ this.state.country } 
                    				 	region={ this.state.region }
                    				 	certifications={ this.state.certifications }
                    				 	form={ this.state.form }
                    				 	/>
                    		
                    		})
                    	}
                    
                    		


                    	<AddButton states={ this.state } updateEntries={ this.updateEntries }/>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

         <div className="col-lg-1 col-md-1 col-sm-1">
        	<div className="container-fluid sticky-top">
          		<div className="row input-div-card">
            		<div className="col-12 mt-2">

            		</div>
          		</div>
        	</div>
      	</div>

			</div>)
          }

}

export default Form;
