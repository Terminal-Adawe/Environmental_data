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
			return <TextInput rowKey={props.rowKey} tag={props.tag} handleInputChanged={ props.handleInputChanged } form={ props.form }/>
		} else if (props.tag.inputtype=='date'){
			return <DateInput tag={props.tag} handleInputChanged={ props.handleInputChanged } form={ props.form } />
		} else if (props.tag.inputtype=='dropdown'){
			return <DropdownInput tag={props.tag} handleInputChanged={ props.handleInputChanged } certifications={ props.certifications } form={ props.form } />
		} else if (props.tag.inputtype=='country-dropdown'){
			return <CountryDropdownInput tag={props.tag} countrydropdownChange={ props.countrydropdownChange } country={ props.country } region={ props.region } form={ props.form }/>
		} else if (props.tag.inputtype=='checkbox'){
			return <CheckBox tag={props.tag} handleInputChanged={ props.handleInputChanged } form={ props.form }/>
		} else if (props.tag.inputtype=='image'){
			return <ImageInput tag={props.tag} handleImageChange={ props.handleImageChange } form={ props.form }/>
		} else if (props.tag.inputtype=='add-more'){
			return <AddMoreButtonInput tag={props.tag} handleAddInputButtonClick={ props.handleAddInputButtonClick } form={ props.form } />
		} else if (props.tag.inputtype=='desc'){
			return <Desc tag={props.tag} />
		} else if (props.tag.inputtype=='' || props.tag.inputtype == "textarea"){
			console.log("Nothing to render..")
			return <></>
		}
	}

function Desc(props){
	return <div className="row mx-1">{ props.tag.placeholder }</div>
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
                        		// Loop through tags one at a time
                          		props.tag.map((formField,i)=>{
                          			// console.log(formField)
                          			return <React.Fragment key={ i }> 
                          			{
                          				formField.map((formFieldz,r)=>{
										return <div key={r} className={columnNo}>
											{ formFieldz.showlabel==1 ? <Label tag={ formFieldz } /> : <Label tag=""/> }
											<Inputs tag={ formFieldz } 
												handleInputChanged={ props.handleInputChanged } 
												handleImageChange={ props.handleImageChange }
												handleAddInputButtonClick = { props.handleAddInputButtonClick }
												country={ props.country } 
												region={ props.region }
												countrydropdownChange={ props.countrydropdownChange }
												form={ props.form }
												rowKey={ formFieldz.position }
												/></div>
                          			})
                          			}
                          			<hr/>
                          			</React.Fragment>
                          			
                          		})
                        	}
                      </div>
            	</div>
	}


function AddMoreButtonInput(props){
	return <button type="button" className="btn btn-primary btn-block add-more-btn" onClick={(e)=>props.handleAddInputButtonClick(e, props.tag.name)}>
				Add More
			</button>
}


function TextInput(props){
		var value = ""
		if(props.form.[props.tag.name]){  
			if(props.tag.type === "array") { 
				// console.log("check if "+props.form.[props.tag.name][[props.form.[props.tag.name].length-1]][0]+" is equal to "+props.form.[props.tag.name].length-1)
				// if(props.form.[props.tag.name][[props.form.[props.tag.name].length-1]][0] == props.form.[props.tag.name].length-1){
				// 	value = props.form.[props.tag.name][[props.form.[props.tag.name].length-1]][1];

				// } 
				
				
			} else {
				value = props.form.[props.tag.name]
				// console.log("For "+props.form.[props.tag.name]+", using "+value)
			 }
		} else {} 

		// console.log("Final value is ")
		// 		console.log(value)

		return  <input 
					type="text" 
					placeholder={props.tag.placeholder} 
					name={props.tag.name} 
					defaultValue={ value }
					className="input-element" 
					onChange={(e)=>props.handleInputChanged(e, props.rowKey)}
					required />

	}

function ImageInput(props){
		return  <input 
					type="file" 
					id="image" 
					placeholder={props.tag.placeholder} 
					name={props.tag.name} 
					defaultValue={ props.form.[props.tag.name] }
					className="input-element" 
					onChange={(e)=>props.handleImageChange(e)}
					multiple="multiple"
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

		return <select id={props.tag.name} name={props.tag.name} defaultValue={ props.form.[props.tag.name] } className="input-element" onChange={(e)=>props.handleInputChanged(e)}>
					<option value=""></option>
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
				location: "",
			},
			url: '',
			image_url:'add/upload_image/',
			trigger: true,
			hiddencheck: '',
		}

		this.Grease_and_hydocarbon_spillageTags = this.Grease_and_hydocarbon_spillageTags.bind(this)
		this.storage_facilitiesTags = this.storage_facilitiesTags.bind(this)
		this.Waste_ManagementTags = this.Waste_ManagementTags.bind(this)
		this.IncenerationTags = this.IncenerationTags.bind(this)
		this.Liquid_waste_oilTags = this.Liquid_waste_oilTags.bind(this)
		this.Safety_trainingTags = this.Safety_trainingTags.bind(this)
		this.Energy_managementTags = this.Energy_managementTags.bind(this)
		this.Health_and_hygiene_awarenessTags = this.Health_and_hygiene_awarenessTags.bind(this)
		this.Slope_stabilization_and_surface_water_retentionTags = this.Slope_stabilization_and_surface_water_retentionTags.bind(this)
		this.Safety_trainingTags = this.Safety_trainingTags.bind(this)
		this.Safety_toolsTags = this.Safety_toolsTags.bind(this)
		this.Complaints_registerTags = this.Complaints_registerTags.bind(this)
		this.Safety_permission_systemTags = this.Safety_permission_systemTags.bind(this)
		this.water_management = this.water_management.bind(this)


		this.toggleLoader = this.toggleLoader.bind(this)
		this.handleInputChanged = this.handleInputChanged.bind(this)
		this.countrydropdownChange = this.countrydropdownChange.bind(this)
		this.handleImageChange = this.handleImageChange.bind(this)
		this.handleAddInputButtonClick = this.handleAddInputButtonClick.bind(this)
		this.updateEntries = this.updateEntries.bind(this)
		this.submitForm = this.submitForm.bind(this)
		this.getCookie = this.getCookie.bind(this)

		this.arrayArranger = this.arrayArranger.bind(this)
		this.tagDeclaration = this.tagDeclaration.bind(this)
		this.setUrl = this.setUrl.bind(this)



		this.formRef = React.createRef();
	}

	componentDidMount(){
		var location = this.props.location

		console.log("Form Mounted. Location is ")
		console.log(location)

		const formType = document.getElementById("form_type").value

		this.setState({
			formtype: formType
		},()=>{
		if (this.state.formtype=="storage_facility"){
			console.log("Storage chosen")
			this.storage_facilitiesTags()
		} else if (this.state.formtype=="Grease_and_hydocarbon"){
			console.log("Grease_and_hydocarbon_spillage chosen")
			this.Grease_and_hydocarbon_spillageTags()
		} else if (this.state.formtype=="Waste_Management"){
			console.log("Waste_Management chosen")
			this.Waste_ManagementTags()
		} else if (this.state.formtype=="Inceneration"){
			console.log("Inceneration chosen")
			this.IncenerationTags()
		} else if (this.state.formtype=="liquid_waste_and_oil"){
			console.log("Liquid_waste_oil chosen")
			this.Liquid_waste_oilTags()
		} else if (this.state.formtype=="health_and_hygiene_awareness"){
			console.log("Health_and_hygiene_awareness likely chosen...")
			this.Health_and_hygiene_awarenessTags()
		} else if (this.state.formtype=="energy_management"){
			console.log("Energy_management chosen")
			this.Energy_managementTags()
		} else if (this.state.formtype=="complaints_register"){
			console.log("Complaints_register chosen")
			this.Complaints_registerTags()
		} else if (this.state.formtype=="slope_stabilization"){
			console.log("Slope_stabilization_and_surface_water_retention chosen")
			this.Slope_stabilization_and_surface_water_retentionTags()
		} else if (this.state.formtype=="safety_training"){
			console.log("Safety_training chosen")
			this.Safety_trainingTags()
		} else if (this.state.formtype=="safety_permission_system"){
			console.log("Safety_permission_system chosen")
			this.Safety_permission_systemTags()
		} else if (this.state.formtype=="safety_tools"){
			console.log("Safety_tools chosen")
			this.Safety_toolsTags()
		} else if (this.state.formtype=="geo_reference"){
			console.log("geo_reference chosen")
			this.geo_reference()
		} else if (this.state.formtype=="fuel_farm"){
			console.log("fuel_farm chosen")
			this.fuel_farm()
		} else if (this.state.formtype=="work_env_compliance"){
			console.log("work_env_compliance chosen")
			this.work_env_compliance()
		} else if (this.state.formtype=="warehouse"){
			console.log("warehouse chosen")
			this.warehouse()
		} else if (this.state.formtype=="conveyers"){
			console.log("conveyers chosen")
			this.conveyers()
		} else if (this.state.formtype=="incident_report"){
			console.log("incident_report chosen")
			this.incident_report()
		} else if (this.state.formtype=="water_management"){
			console.log("water_management chosen")
			this.water_management()
		} 

		})
		
	}

	componentDidUpdate(prevProps, prevState){
    	// if(prevState.value != this.state.value){
    	// 	console.log("reloading")
    	// 	// console.log(this.state.name)
    	// 	let form = this.state.form

    	// 	if(this.state.name == "projects[]"){
    	// 		// Form switch to trigger when a project id in the form matches the project id
    	// 		// in the props
    	// 		let switche = 0;
    	// 		form.projects.map((project,i)=>{
    	// 			// console.log("The project is ")
    	// 			// console.log(project[0])
    	// 			// console.log(" compared with ")
    	// 			// console.log(this.state.value[0])
    	// 			if(project[0]==this.state.value[0]){
    	// 				project[1] = this.state.value[1]
    	// 				switche = 1
    	// 			}
    	// 		})

    	// 		if(switche==0){
    	// 			// console.log("Projects are ")
    	// 			// console.log(form.projects)
    	// 			// console.log(this.state.value)
    	// 			// console.log(form)
    	// 			// console.log("Length of the project array is ")
    	// 			// console.log(form.projects.length)
    	// 			const projectArrayLength = form.projects.length
    	// 			// form.projects[0] != "" ? form.projects = [...form.projects, form.projects[0]] : ""
    	// 			// form.projects = [...form.projects, this.props.states.value]
  
    	// 				form.projects = [...form.projects, this.state.value]

    				
    	// 		}
    	// 	} else if(this.state.name == "duties[]"){
    	// 		// Form switch to trigger when a project id in the form matches the project id
    	// 		// in the props
    	// 		let switche = 0;
    	// 		form.duties.map((duty,i)=>{
    	// 			console.log("The duties is ")
    	// 			console.log(duty)
    	// 			// console.log(" compared with ")
    	// 			// console.log(this.state.value[0])
    	// 			if(duty[0]==this.state.value[0]){
    	// 				duty[1] = this.state.value[1]
    	// 				switche = 1
    	// 			}
    	// 		})

    	// 		if(switche==0){
    	// 			// console.log("Duties are ")
    	// 			// console.log(form.duties)
    	// 			// console.log(this.state.value)
    	// 			// console.log(form)
    	// 			// console.log("Length of the duty array is ")
    	// 			// console.log(form.duties.length)
    	// 			const dutyArrayLength = form.duties.length
    	// 			// form.projects[0] != "" ? form.projects = [...form.projects, form.projects[0]] : ""
    	// 			// form.projects = [...form.projects, this.props.states.value]
  
    	// 				form.duties = [...form.duties, this.state.value]

    				
    	// 		}
    	// 	}
    	// 	else {
    	// 		form.[this.state.name] = this.state.value
    	// 	}

    	// 	console.log("Form is ")
    	// 	console.log(form)


    	// 	this.setState({
    	// 		form: form
    	// 	})

    	// 	// console.log("updated form is ")
    	// 	// console.log(this.state.form)
    	// }

    	if(prevProps.location != this.props.location){
    		var form = this.state.form

    		form.location = this.props.location

    		// console.log('new form with location is ')
    		// console.log(form)

    		this.setState({
    			form: form
    		})
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


	toggleLoader(state){
    	this.props.loader(state)
    }



	tagDeclaration(tags){
		this.setState({
			tags: tags
		},()=>{
			let form = this.state.form
			const formKeys = Object.keys(form)

			// console.log("Tags is ")
			// console.log(tags)

			tags.map((tag,t)=>{
				console.log("tags are")
				console.log(tag.formField)
				loop1:
				for(var i=0; i<tag.formField.length; i++){

					if(form.[tag.formField[i][0].name] && tag.formField[i][0].type){
						// console.log("Comparing...")
						// console.log(tag.formField[i][0].name)
						// console.log(" and ")
						// // console.log(formKeys)


						// if(tag.formField[i][0].type=="array"){
						// 		// console.log("Length is ")
						// 		// console.log(form.[field[0].name].length)
						// 		// console.log("Print out tag")
						// 		// console.log(tag.formField[i][0])
						// 	loop2:
						// 	for(var r=0; r< formKeys.length; r++){
						// 		if(formKeys[r] == tag.formField[i][0].name){
						// 			console.log(formKeys[r])
						// 			console.log("They match so adding this to the array ")
						// 			console.log(form.[tag.formField[i][0].name])
						// 			form.[tag.formField[i][0].name] = [...form.[tag.formField[i][0].name], [form.[tag.formField[0][i].name].length,""]]

						// 			break loop1;
						// 		}
						// 	}

							
						// }
					} else 
					// Form field name does not exist. Add it.
					{
						// console.log("I'm checking type ..")
						// Check if field has a type parameter
						if(tag.formField[i][0].type){
							if(tag.formField[i][0].type=="array"){
								// console.log("I'm an array..")
								form.[tag.formField[i][0].name] = [[0,""]] 
							} else {
								// console.log("I'm not an array ..")
								form.[tag.formField[i][0].name] = "" 
							}
						} else {
							// console.log("How come???")
							if(tag.formField[i][0].name!=""){
								form.[tag.formField[i][0].name] = "" 
							}
						}
						
					}
				}
			})

			console.log("This form after manipulation is ")
			console.log(form)

			this.setState({
				form: form
			})
		})
	}

	setUrl(url){
		this.setState({
				url: url
			})
	}



	storage_facilitiesTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Seepage point showing the amount of seepage of the dam walls.',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'status_of_seepage_point',placeholder:'',label:'Status of Seepage Point',showlabel:1,options:[['Good','Good'],['Slightly Disturbed','Slightly Disturbed'],['Blocked','Blocked']]}]]},
			{formField: [[{inputtype:'dropdown',name:'stability_of_dam_walls',placeholder:'',label:'Stability of Dam Walls',showlabel:1,options:[['Stable','Stable'],['Signs of Erosion','Signs of Erosion'],['Rehabilitated','Rehabilitated']]}]]},
			{formField: [[{inputtype: 'text', name:'holding_capacity',placeholder:'Enter Holding Capacity',label:'Holding Capacity',showlabel:1}]]},
			{formField: [[{inputtype:'text',name:'current_capacity',placeholder:'Enter Current Capacity',label:'Current Capacity',showlabel:1}]]},
			{formField: [[{inputtype:'text',name:'spillways_capacity',placeholder:'Enter Spillways Capacity',label:'Spillways Capacity',showlabel:1}]]},
			{formField: [[{inputtype:'text',name:'spillways_stability',placeholder:'Enter Spillways Stability',label:'Spillways Stability',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'signs_of_erosion_spillway_tip',placeholder:'Erosion Signs',label:'Signs of Erosion on Spillway Tip',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
		]

		const action_url = 'add/add-seepage/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Grease_and_hydocarbon_spillageTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Grease and Hydrocarbon storage condition',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'storage_condition',placeholder:'',label:'Storage Condition',showlabel:1,options:[['Completely Impervious Surface','Completely Impervious Surface'],['Partially Impervious','Partially Impervious'],['Non Impervious','Non Impervious'],['Stored in Containment','Stored in Containment'],['Not Stored in Containment','Not Stored in Containment']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-grease-and-hydrocarbon/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Waste_ManagementTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Waste management data.',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'segregation_at_source_and_bins',placeholder:'',label:'Segregation at source and use of colored bins',showlabel:1,options:[['Effective','Effective'],['Not Effective','Not Effective'],['Partially Effective','Partially Effective'],['Sorted at Dump Site','Sorted at Dump Site']]}]]},
			{formField: [[{inputtype: 'text', position:0, name:'glass_waste_source',type:'array',placeholder:'Source',label:'Glass waste source',showlabel:1}],[{inputtype: 'text', position:0, type:'array', name:'glass_waste_weight',placeholder:'Weight',label:'Glass waste weightage',showlabel:1}],[{inputtype: 'add-more', name:'glass_waste'}]]},
			{formField: [[{inputtype: 'text', position:0, name:'plastic_waste_source',type:'array',placeholder:'Source',label:'Plastic waste source',showlabel:1}],[{inputtype: 'text', position:0, type:'array', name:'plastic_waste_weight',placeholder:'Weight',label:'Plastic waste weightage',showlabel:1}],[{inputtype: 'add-more', name:'plastic_waste'}]]},
			{formField: [[{inputtype: 'text', position:0, name:'metal_waste_source',type:'array',placeholder:'Source',label:'Metal waste source',showlabel:1}],[{inputtype: 'text', position:0, type:'array', name:'metal_waste_weight',placeholder:'Weight',label:'Metal waste weightage',showlabel:1}],[{inputtype: 'add-more', name:'metal_waste'}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-waste-management/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	IncenerationTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Incineration.',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'items_incenerated',placeholder:'Item name',label:'Item',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'quantity',placeholder:'Quantity',label:'Quantity',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'temperature',placeholder:'Temperature',label:'Temperature',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-inceneration/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Liquid_waste_oilTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Liquid waste oil',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'discharge_point',placeholder:'Effluent Discharge Point',label:'Effluent Discharge Point',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'source',placeholder:'',label:'Source',showlabel:1,options:[['Maintenance Workshop','Maintenance Workshop'],['Other Area','Other Area']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-liquid-waste-oil/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Health_and_hygiene_awarenessTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Health and Hygiene awareness involving the staff',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'training',placeholder:'Training title',label:'Training title',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'no_of_staff',placeholder:'Number of Staff',label:'Number of staff',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'no_of_visitors',placeholder:'Number of Visitors',label:'Number of Visitors',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'duration',placeholder:'Duration of training',label:'Training duration',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-health-and-hygiene-awareness/'

	    console.log("Health and hygeine tags section")

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Energy_managementTags(){
		console.log("I have been called")
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Energy consumption in the camp',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'total_energy_available',placeholder:'Total Energy Available',label:'Total Energy Available',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'camp_consumption',placeholder:'Camp Consumption',label:'Camp Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'admin_consumption',placeholder:'Admin Consumption',label:'Admin Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'workshop_consumption',placeholder:'Workshop Consumption',label:'Workshop Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'mine_plant_consumption',placeholder:'Mine Plant Consumption',label:'Mine Plant Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'other_consumption',placeholder:'Other Consumption',label:'Other Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-energy-management/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	water_management(){
		console.log("I have been called")
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Water consumption in the camp',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'total_water_quantity_available',placeholder:'Total Water Quantity Available',label:'Total Water Quantity Available',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'camp_consumption',placeholder:'Camp Consumption',label:'Camp Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'cafeteria_consumption',placeholder:'Cafeteria Consumption',label:'Cafeteria Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'admin_consumption',placeholder:'Admin Consumption',label:'Admin Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'workshop_consumption',placeholder:'Workshop Consumption',label:'Workshop Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'mine_plant_consumption',placeholder:'Mine Plant Consumption',label:'Mine Plant Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'other_consumption',placeholder:'Other Consumption',label:'Other Consumption',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-water-management/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Complaints_registerTags(){
		console.log("Complaints tags have been called")
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Do people complain?',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'no_of_complaints',placeholder:'Number of complaints',label:'Number of complaints',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'status_of_complaints',placeholder:'',label:'Status',showlabel:1,options:[['Resolved','Resolved'],['Pending','Pending'],['Other (State reason in comments)','Other']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-complaints-register/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Slope_stabilization_and_surface_water_retentionTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Slope stabilization and surface water retention',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'no_of_exposed_unstabilized_slopes',placeholder:'Number of exposed unstabilized slopes',label:'Number of exposed unstabilized slopes',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'status',placeholder:'',label:'Source',showlabel:1,options:[['Stabilized','Stabilized'],['Working Progress','Working Progress'],['Pending','Pending'],['Other (State reason in comments)','Other']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-slope-stabilization/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Safety_trainingTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Training details if any.',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'training',placeholder:'Training title',label:'Training title',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'no_of_staff',placeholder:'Number of Staff',label:'Number of staff',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'no_of_inductions',placeholder:'Number of Inductions',label:'Number of Inductions',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'no_of_visitors',placeholder:'Number of Visitors',label:'Number of Visitors',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'duration',placeholder:'Duration of training',label:'Training duration',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-safety-training/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Safety_permission_systemTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Safety Pemitting records',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'no_of_permits_issued',placeholder:'Number of permits issued',label:'Number of permits issued',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'status',placeholder:'',label:'Status',showlabel:1,options:[['Work Ended Safely','Work Ended Safely'],['Work did not end safely','Work did not end safely']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-safety-permission-system/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	Safety_toolsTags(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Safety Tools available',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'no_of_estinquishers',placeholder:'Number of Estinguishers',label:'Number of Estinguishers',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'fire_alarm',placeholder:'',label:'Fire Alarm',showlabel:1,options:[['Active','Active'],['Not Active','Not Active']]}]]},
			{formField: [[{inputtype:'dropdown',name:'status_of_estinguishers',placeholder:'',label:'Status of Estinguishers',showlabel:1,options:[['Mine','Mine'],['Port','Port'],['Serviced','Serviced'],['Expired','Expired']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Any Comment?',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-safety-tools/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	geo_reference(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Reference this point and write a description of what may be interesting here',label:'',showlabel:0}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Reference description',label:'Description',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-reference-point/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	fuel_farm(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Status of the fuel farms on site.',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'spillage_status',placeholder:'',label:'Spillage Status',showlabel:1,options:[['No Spillage','No Spillage'],['High Spillage','High Spillage'],['Low Spillage','Low Spillage']]}]]},
			{formField: [[{inputtype:'dropdown',name:'impervious_status',placeholder:'',label:'Impervious Status',showlabel:1,options:[['Not Impervious','Not Impervious'],['Impervious','Impervious'],['Semi Impervious','Semi Impervious']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'comment',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]

		const action_url = 'add/add-fuel-farm-data/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	work_env_compliance(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Work environment compliance.',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'first_aid',placeholder:'',label:'First Aid Available?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype:'dropdown',name:'safety_stickers',placeholder:'',label:'Safety Stickers Available?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype:'dropdown',name:'estinguishers',placeholder:'',label:'Fire Estinguishers Available?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype: 'text', name:'no_of_estinquishers',placeholder:'Number of Fire Estinguishers',label:'Number of Fire Estinguishers',showlabel:1}]]},
			{formField: [[{inputtype:'dropdown',name:'fire_alarm',placeholder:'',label:'Fire Alarms Available?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype:'dropdown',name:'flooding',placeholder:'',label:'Is there flooding?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype:'dropdown',name:'flammables',placeholder:'',label:'Are there any flammables?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Extra Comments',label:'comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]
			
		const action_url = 'add/add-work-environmental-compliance-data/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	warehouse(){
		const tags = [ 
			{formField: [[{inputtype:'desc',name:'',placeholder:'Warehouse details.',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'eye_wash',placeholder:'',label:'Eye wash Available?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype:'dropdown',name:'shower',placeholder:'',label:'Shower Available?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Comment',label:'Description',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]
			
		const action_url = 'add/add-warehouse-data/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	conveyers(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Information about conveyors.',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'electrical_safety_insulation',placeholder:'',label:'Are there Electrical Safety Insulations?',showlabel:1,options:[['Yes','Yes'],['No','No']]}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Comment',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]
			
		const action_url = 'add/add-conveyers-data/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	incident_report(){
		const tags = [
			{formField: [[{inputtype:'desc',name:'',placeholder:'Incident report on an incident that may have taken place.',label:'',showlabel:0}]]},
			{formField: [[{inputtype:'dropdown',name:'incident_category',placeholder:'',label:'Select an incident category',showlabel:1,options:[['Personal Injury','Personal Injury'],['Property Damage','Property Damage'],['Fires','Fires'],['Loss to Process','Loss to Process'],['Environment','Environment'],['Near Miss','Near Miss'],['Community','Community'],['Death','Death']]}]]},
			{formField: [[{inputtype: 'text', name:'incident_location',placeholder:'Incident Location',label:'Incident Location',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'victim_name',placeholder:'Victim Name',label:'Victim Name',showlabel:1}]]},
			{formField: [[{inputtype: 'date', name:'incident_start',placeholder:'Incident Start date',label:'Incident Start date',showlabel:1}]]},
			{formField: [[{inputtype: 'date', name:'incident_end',placeholder:'Incident End date',label:'Incident End date',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'cause_of_incident',placeholder:'Cause of Incident',label:'Cause of Incident',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'actions_taken_immediately',placeholder:'Actions Taken Immediately',label:'Actions taken Immediately',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'further_actions_taken',placeholder:'Further Actions taken',label:'Further Actions taken',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'corrective_measures',placeholder:'Corrective Measures',label:'Corrective Measures',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'responsible_person',placeholder:'Responsible Person',label:'Responsible Person',showlabel:1}]]},
			{formField: [[{inputtype: 'text', name:'comment',placeholder:'Comment',label:'Comment',showlabel:1}]]},
			{formField: [[{inputtype: 'image', name:'image',placeholder:'',label:'Upload image(s)',showlabel:1}]]},
			]
			
		const action_url = 'add/add-incident-report/'

		this.tagDeclaration(tags)
		this.setUrl(action_url)
	}

	// Reposition arrays in forms
	arrayArranger(array, inputLength){
		array = [...array, [array.length,""]]
			
			// Rearrange array
			for(var i=inputLength; i > 0; i--){
				if(i==0){
					array[i][1] = ""
					array[i][1] = ""
				} else {
					array[i][1] = array[i-1][1]
					array[i][1] = array[i-1][1]
				}
			}
			//

			return array
	}

	handleAddInputButtonClick(e, name){
		var tags = this.state.tags
		let inputs = []

		var inputLength = document.getElementsByName(name).length

		let form = this.state.form
		const formKeys = Object.keys(form)

		if(name=="glass_waste"){
			inputLength = document.getElementsByName("glass_waste_source").length
			inputs = {formField: [[{inputtype: 'text', position:inputLength, name:'glass_waste_source',type:'array',placeholder:'Source',label:'Glass waste source',showlabel:1}],[{inputtype: 'text', type:'array', name:'glass_waste_weight',placeholder:'Weight',label:'Glass waste weightage',showlabel:1}],[{inputtype: '', name:'glass_waste'}]]}

			form.glass_waste_source = this.arrayArranger(form.glass_waste_source,inputLength)
			form.glass_waste_weight = this.arrayArranger(form.glass_waste_weight,inputLength)

		}

		if(name=="plastic_waste"){
			inputLength = document.getElementsByName("plastic_waste_source").length
			inputs = {formField: [[{inputtype: 'text', position:inputLength, name:'plastic_waste_source',type:'array',placeholder:'Source',label:'Plastic waste source',showlabel:1}],[{inputtype: 'text', type:'array', name:'plastic_waste_weight',placeholder:'Weight',label:'Plastic waste weightage',showlabel:1}],[{inputtype: '', name:'plastic_waste'}]]}
			
			form.plastic_waste_source = this.arrayArranger(form.plastic_waste_source,inputLength)
			form.plastic_waste_weight = this.arrayArranger(form.plastic_waste_weight,inputLength)
		

		}

		if(name=="metal_waste"){
			inputLength = document.getElementsByName("metal_waste_source").length
			inputs = {formField: [[{inputtype: 'text', position:inputLength, name:'metal_waste_source',type:'array',placeholder:'Source',label:'Metal waste source',showlabel:1}],[{inputtype: 'text', type:'array', name:'metal_waste_weight',placeholder:'Weight',label:'Metal waste weightage',showlabel:1}],[{inputtype: '', name:'metal_waste'}]]}
			
			form.metal_waste_source = this.arrayArranger(form.metal_waste_source,inputLength)
			form.metal_waste_weight = this.arrayArranger(form.metal_waste_weight,inputLength)
		}

		console.log("inputs length is ")
		console.log(inputLength)

		tagLoop:
		for(var i=0; i<tags.length; i++){

			formLoop:
			for (var r=0; r<tags[i].formField.length; r++){
				var formName = tags[i].formField[r]


				if(formName[0].name == name){

					// console.log("Form name matches")
					// console.log(formName[0].name+" v "+name)
					tags.splice(i, 0, inputs);

					break tagLoop;
				}
			}
				
			}

			console.log(tags)
		
	this.tagDeclaration(tags)

	}

	handleInputChanged(e, r){
		console.log("triggerd")
		// console.log(e.target.name)

		// console.log(e.target.value)

		// console.log(e.target.type)

		// console.log(r)

		let form = this.state.form



		let value = e.target.type === 'checkbox' ? e.target.checked : e.target.value;

		// console.log("Value recorded is ")
		// console.log(value)

		if(e.target.name === "glass_waste_source" || e.target.name === "glass_waste_weight" || e.target.name === "plastic_waste_source" || e.target.name === "plastic_waste_weight" || e.target.name === "metal_waste_source" || e.target.name === "metal_waste_weight"){

			value = [r,e.target.value]

			var formName = form.[e.target.name]

			console.log("Form name tag is ")
			console.log(formName)

			let switche = 0;
    			formName.map((target,i)=>{
    				console.log("The target is ")
    				console.log(target[0])
    				console.log(" compared with ")
    				console.log(value[0])
    				if(target[0]==value[0]){
    					target[1] = value[1]
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
    				const dutyArrayLength = form.[e.target.name].length
    				// form.projects[0] != "" ? form.projects = [...form.projects, form.projects[0]] : ""
    				// form.projects = [...form.projects, this.props.states.value]
  
    					form.[e.target.name] = [...form.[e.target.name], this.state.value]

    				
    			}

    			// console.log("new form is ")
    			// console.log(form)

		} else {
			// console.log("Target name is ")
			// console.log(form.[e.target.name])
			// console.log(" and value is ")
			// console.log(value)
			form.[e.target.name] = value
		}

		console.log("form with values is ")
		console.log(form)



		this.setState({
			name: e.target.name,
			value: value,
			form: form
		})
	}

	handleImageChange(e){

		this.setState({
			name: e.target.name,
			value: e.target.files,
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

		return (<div className="row">
				<div className="col-lg-11 col-md-11 col-sm-12">
        <div className="card input-div-card">
          <div className="card-body">
            <div className="container-fluid">
            	<div id="error-message">
            	</div>
            	<div id="success-message">
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
                    				 	handleImageChange={ this.handleImageChange }
                    				 	handleAddInputButtonClick = { this.handleAddInputButtonClick } 
                    				 	countrydropdownChange={ this.countrydropdownChange } 
                    				 	country={ this.state.country } 
                    				 	region={ this.state.region }
                    				 	certifications={ this.state.certifications }
                    				 	form={ this.state.form }
                    				 	rowKey={i}
                    				 	/>
                    		
                    		})
                    	}
                    
                    		


                    	<AddButton states={ this.state } updateEntries={ this.updateEntries } loader={ this.toggleLoader } baseUrl={ this.props.baseUrl } getLocation={ this.props.getLocation } />
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
