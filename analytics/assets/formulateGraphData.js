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
        this.formulateGraph = this.formulateGraph.bind(this)

	}

	componentDidMount(){
			// console.log("processing graph ... ")
			// console.log(this.props)
            
			let data = []

    		this.props.data ? data = this.checkModule(this.props.module, this.props.graphConfig)

    		: data = []

             // this.props.data ? 
             // data = this.formulateGraph(this.props.graphData)
             // : data = []

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

	checkModule(module, graphConfig){
		// console.log("In module check")
		// console.log(module.module_name)
		let rawData = []
		switch(module.module_name){
			case "storage_facility":
    			rawData = this.props.data.Storage_facility
    			// rawData = this.storage_facility(rawData)
    			break;
    		// case "Grease_and_hydocarbon":
    		// 	rawData = this.props.data.Grease_and_hydocarbon_spillage
    		// 	rawData = this.Grease_and_hydocarbon(rawData)
    		// 	break;
    		case "Inceneration":
    			rawData = this.props.data.Inceneration
    			// rawData = this.Inceneration(rawData)
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
    			// rawData = this.energy_management(rawData)
    			break;
    		case "complaints_register":
    			rawData = this.props.data.Complaints_register
    			// rawData = this.complaints_register(rawData)
    			break;
    		case "slope_stabilization":
    			rawData = this.props.data.Slope_stabilization_and_surface_water_retention
    			// rawData = this.slope_stabilization(rawData)
    			break;
    		case "safety_permission_system":
    			rawData = this.props.data.Safety_permission_system
    			// rawData = this.safety_permission_system(rawData)
    			break;
    		case "safety_training":
    			rawData = this.props.data.Safety_training
    			// rawData = this.safety_training(rawData)
    			break;
    		case "safety_tools":
    			rawData = this.props.data.Safety_tools
    			// rawData = this.safety_tools(rawData)
    			break;
    		case "Waste_Management":
    			rawData = this.props.data.Waste_Management
    			// rawData = this.Waste_Management(rawData)
    			break;
            case "fuel_farm":
                rawData = this.props.data.FuelFarm
                // rawData = this.Waste_Management(rawData)
                break;
            case "work_env_compliance":
                rawData = this.props.data.WorkEnvCompliance
                // rawData = this.Waste_Management(rawData)
                break;
            case "warehouse":
                rawData = this.props.data.Warehouse
                // rawData = this.Waste_Management(rawData)
                break;
            case "Waste_Management":
                rawData = this.props.data.Waste_Management
                // rawData = this.Waste_Management(rawData)
                break;
            case "geo_reference":
                rawData = this.props.data.GeoReferencePoints
                // rawData = this.Waste_Management(rawData)
                break;
            case "fuel_farm":
                rawData = this.props.data.FuelFarm
                // rawData = this.Waste_Management(rawData)
                break;
            case "work_env_compliance":
                rawData = this.props.data.WorkEnvCompliance
                // rawData = this.Waste_Management(rawData)
                break;
            case "warehouse":
                rawData = this.props.data.Warehouse
                // rawData = this.Waste_Management(rawData)
                break;
            case "conveyers":
                rawData = this.props.data.Conveyers
                // rawData = this.Waste_Management(rawData)
                break;
            case "incident_report":
                rawData = this.props.data.IncidentReport
                // rawData = this.Waste_Management(rawData)
                break;
            case "water_management":
                rawData = this.props.data.Water_management
                // rawData = this.Waste_Management(rawData)
                break;
    		default:
    			rawData=""
    			break;
		}

        rawData = this.formulateGraph(rawData, graphConfig)

		return rawData
    				
	}


    formulateGraph(data_x, graphConfig){
        let data = []
            data_x ?
            data_x.map((val, i)=>{
              // console.log("Value given is "+val.current_capacity)
              let x_column = ""
              let y_column = ""
              graphConfig.x_column=="sequence" || graphConfig.graph_type=="Line Chart"
              ? x_column = i
              : x_column = val.[graphConfig.x_column]

              graphConfig.y_column=="sequence" 
              ? y_column = i
              : y_column = val.[graphConfig.y_column]


                  data = [...data, {x: x_column, y: y_column}]
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
			console.log("graph configs are...")
			console.log(this.props.graphConfig)
            let graph = ""
            if(this.props.graphConfig.graph_type == "Line Chart"){
                graph = <LineGraph data={this.state.data} />
            } else if (this.props.graphConfig.graph_type == "Bar Chart"){
                graph = <BarGraph data={this.state.data} />
            }

			return (<React.Fragment>
                <div className="container-fluid">
                    <div className="row graph-name">
                        <h4>{this.props.graphConfig.graph_name}</h4>
                    </div>
                    <div className="row">{ this.props.module.description }</div>
                </div>
                    { graph }
                    </React.Fragment>)
		}
		
	}
}

export default FormulateGraphData