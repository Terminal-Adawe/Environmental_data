import React from 'react';
import ReactDOM from "react-dom";
import BarGraph from './bargraph';
import LineGraph from './linegraph';

import axios from "axios";
import cookie from "react-cookies";


class FormulateGraphData extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
		}

		this.checkModule = this.checkModule.bind(this)
		this.Grease_and_hydocarbon = this.Grease_and_hydocarbon.bind(this)
		this.storage_facility = this.storage_facility.bind(this)

	}

	componentDidMount(prevProps, prevState){
			// console.log("processing graph ... ")
			// console.log(this.props)
			let data = []

    		this.props.data ? data = this.checkModule(this.props.module)

    		: data = []

    		// console.log("manipulated data is ")
    		// console.log(data)
	
			this.setState({
				data: data,
			})
	}

	componentDidUpdate(prevProps, prevState){
		if(prevProps.data != this.props.data){
			// console.log("processing graph 2... ")
			// console.log(this.props)
			let data = []
		
	
			this.setState({
				data: data,
			})
		}
	}

	checkModule(module){
		// console.log("In module check")
		// console.log(module.module_name)
		let rawData = []
		switch(module.module_name){
			case "storage_facility":
    			rawData = this.props.data.Storage_facility
    			rawData = this.storage_facility(rawData)
    			break;
    		// case "Grease_and_hydocarbon":
    		// 	rawData = this.props.data.Grease_and_hydocarbon_spillage
    		// 	rawData = this.Grease_and_hydocarbon(rawData)
    		// 	break;
    		case "Inceneration":
    			rawData = this.props.data.Inceneration
    			rawData = this.Inceneration(rawData)
    			break;
    		// case "liquid_waste_and_oil":
    		// 	rawData = this.props.data.Liquid_waste_oil
    		// 	rawData = this.liquid_waste_and_oil(rawData)
    		// 	break;
    		// case "health_and_hygiene_awareness":
    		// 	rawData = this.props.data.Health_and_hygiene_awareness
    		// 	rawData = this.health_and_hygiene_awareness(rawData)
    		// 	break;
    		case "energy_management":
    			rawData = this.props.data.Energy_management
    			rawData = this.energy_management(rawData)
    			break;
    		case "complaints_register":
    			rawData = this.props.data.Complaints_register
    			rawData = this.complaints_register(rawData)
    			break;
    		case "slope_stabilization":
    			rawData = this.props.data.Slope_stabilization_and_surface_water_retention
    			rawData = this.slope_stabilization(rawData)
    			break;
    		case "safety_permission_system":
    			rawData = this.props.data.Safety_permission_system
    			rawData = this.safety_permission_system(rawData)
    			break;
    		case "safety_training":
    			rawData = this.props.data.Safety_training
    			rawData = this.safety_training(rawData)
    			break;
    		case "safety_tools":
    			rawData = this.props.data.Safety_tools
    			rawData = this.safety_tools(rawData)
    			break;
    		case "Waste_Management":
    			rawData = this.props.data.Waste_Management
    			rawData = this.Waste_Management(rawData)
    			break;
    		default:
    			rawData=""
    			break;
		}

		return rawData
    				
	}

	storage_facility(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.current_capacity)
    		      data = [...data, {'x': i, 'y': val.current_capacity}]
    		    })
    		  : ""

    		  return data
	}

	Grease_and_hydocarbon(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.current_capacity)
    		      data = [...data, {'x': i, 'y': val.current_capacity}]
    		    })
    		  : ""

    		  return data
	}

	Waste_Management(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.glass_waste_source )
    		      data = [...data, {'x': i, 'y': val.glass_waste_weight }]
    		    })
    		  : ""

    		  return data
	}

	Inceneration(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.items_incenerated)
    		      data = [...data, {'x': i, 'y': val.items_incenerated}]
    		    })
    		  : ""

    		  return data
	}

	liquid_waste_and_oil(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.current_capacity)
    		      data = [...data, {'x': i, 'y': val.current_capacity}]
    		    })
    		  : ""

    		  return data
	}

	health_and_hygiene_awareness(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.no_of_staff )
    		      data = [...data, {'x': val.training, 'y': val.no_of_staff }]
    		    })
    		  : ""

    		  return data
	}

	energy_management(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.total_energy_available )
    		      data = [...data, {'x': i, 'y': val.total_energy_available }]
    		    })
    		  : ""

    		  return data
	}

	complaints_register(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.no_of_complaints)
    		      data = [...data, {'x': i, 'y': val.no_of_complaints}]
    		    })
    		  : ""

    		  return data
	}

	slope_stabilization(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.no_of_exposed_unstabilized_slopes)
    		      data = [...data, {'x': i, 'y': val.no_of_exposed_unstabilized_slopes}]
    		    })
    		  : ""

    		  return data
	}

	safety_permission_system(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.no_of_permits_issued)
    		      data = [...data, {'x': i, 'y': val.no_of_permits_issued}]
    		    })
    		  : ""

    		  return data
	}

	safety_training(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.no_of_inductions)
    		      data = [...data, {'x': i, 'y': val.no_of_inductions}]
    		    })
    		  : ""

    		  return data
	}

	safety_tools(rawData){
			let data = []
			rawData ?
    		rawData.map((val, i)=>{
    		  // console.log("Value given is "+val.no_of_estinquishers )
    		      data = [...data, {'x': i, 'y': val.no_of_estinquishers }]
    		    })
    		  : ""

    		  return data
	}


	


	render(){
		if (!Array.isArray(this.state.data) || !this.state.data.length) {
  			// array does not exist, is not an array, or is empty
  			// ⇒ do not attempt to process array
  	// 		console.log("No Array...")
			// console.log(this.state.data)
  			return (<></>)
		} else {
			// console.log("Array...")
			// console.log(this.state.data)
			return (<React.Fragment><div>{ this.props.module.description }</div><LineGraph data={this.state.data} /></React.Fragment>)
		}
		
	}
}

export default FormulateGraphData