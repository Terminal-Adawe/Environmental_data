import React from 'react';
import ReactDOM from "react-dom";
import Widgets_custom from './widget_custom';
import Widgets_a from './widget1';
import Widgets_b from './widget2';
import Widgets_c from './widget3';
import FormulateGraphData from './formulateGraphData';

import axios from "axios";
import cookie from "react-cookies";

function ColumnMaker(props){
	
	// console.log("Props are ")
	// console.log(props.data.Storage_facility)
	// console.log(props)

	
  let data = ""
  let module_name = ""

  props.data ? data = props.data : data = ""
  props.module.descriptions ? module_name=props.module.description : ""

  console.log("module name is "+data)
  console.log(data)
									
		return (<div className="col-lg-6 col-sm-12 my-4">
              <div className="card graph-card my-2">
                <div className="card-body">
                  <FormulateGraphData data={data} module={props.module} graphConfig={ props.graphConfig }/>
                </div>
                <hr/>
                {
                props.view == "graph" ?
                  <div className="container-fluid my-3">
              <div className="row mb-4">
                <div className="col-lg-4 col-md-4 col-sm-6">
                  <label className="form-check-label predictive_label mx-4">
                    <h5>Show on dashboard</h5>
                    <input 
                      type="checkbox" 
                      className="form-check-input current input-element" 
                      name="on_dashboard" 
                      defaultChecked={props.graphConfig.on_dashboard} 
                      onChange={(e)=>props.handleCheckboxInputChanged(e, props.graphConfig.id)}
                      />
                  </label>
                </div>
                <div className="col-lg-6 col-md-6 col-sm-6">
                  <div className="row mt-1">
                    <div className="col-lg-6 col-md-6 col-sm-6">
                      <span className="mx-4">
                        <a href="analytics/view-graph">Edit Graph</a>
                      </span>
                    </div>
                    <div className="col-lg-6 col-md-6 col-sm-6">
                      <span className="mx-4">
                        <a href="#">Add to Report</a>
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              </div>
                : ""
              }
              </div>
              
              
            </div>)
									
								
	}


function Widget_generator(props){
  return (<div className="container-fluid">
            <div className="row">
          {
            props.widgets.map((widget,i)=>{
              return <div className="col-lg-4 col-sm-12">
              <Widgets_custom compliance={ props.data.ComplianceValue } parameter={ widget[0] } background={ widget[1] } />
              </div>
            })
          }
          </div>
       </div>)
} 



class Template extends React.Component {
	constructor(){
		super()

    this.state={
      widget1: "Turbidity",
      widget2: "Chemical Oxygen Demand",
      widget3: "Total Arsenic",
      widgets: [["Turbidity","#17c1f3"],["Chemical Oxygen Demand","#f0be08"],["Total Arsenic","#bb8fce"]],
      url: 'analytics/add/update-graph-config/'
    }

    this.handleCheckboxInputChanged = this.handleCheckboxInputChanged.bind(this)
    this.setDashboard = this.setDashboard.bind(this)
	}


  handleCheckboxInputChanged(e, id){
    console.log("value is ")
    console.log(id)
    console.log(e.target.checked)

    this.setDashboard(e.target.checked, id)
  }

  setDashboard(value,id){
    const url = this.state.url
    const baseUrl = this.props.baseUrl
    let form_data = new FormData();


    form_data.append('value', value)
    form_data.append('id', id)

    axios.post(`${baseUrl}/${url}`,form_data,{
                    headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                     enctype: 'multipart/form-data'
                    },
                })
                .then(response => {
                    console.log("graph response is ")
                    console.log(response)

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
		return (<div className="row">
					<div className="col-12">
						<div className="row">
              {
                this.props.view=="dashboard" ? <Widget_generator data={ this.props.data } widgets={ this.state.widgets } module={ this.props.module } parameter={ this.state.widget1 } /> : ""
              }
                      
								
                {
                  this.props.data.Graph_config ? 
                  this.props.data.Graph_config.filter(config=>((this.props.view=="dashboard" && config.on_dashboard==1) || this.props.view=="graph")).map((graph,i)=>{
                    return <React.Fragment key={i}>
                    {
                      this.props.data.modules ?
                      this.props.data.modules.filter(module=>(module.id==graph.module && this.props.module=="all") || (module.id==graph.module && module.module_name==this.props.module)).map((module,i)=>{
                        return <ColumnMaker key={i} data={ this.props.data } module={ module } graphConfig={ graph } handleCheckboxInputChanged={ this.handleCheckboxInputChanged } view={this.props.view}/>
                      })
                    : ""
                    }
                    </React.Fragment>
                    
                  }) : ""
                }
						</div>
					</div>
  			</div>)
	}
}

export default Template