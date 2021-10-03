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
	// console.log(props.data)
	// console.log(props)

	
  let data = ""
  let module_name = ""

  props.data ? data = props.data : data = ""
  props.module.descriptions ? module_name=props.module.description : ""

  // console.log("module name is "+data)
  // console.log(data)
  // console.log(props.module)

									
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
                        <a href="#" data-toggle="modal" data-target="#edit-graph" onClick={ (e)=>props.editGraph(e,props.graphConfig) }>Edit Graph</a>
                      </span>
                    </div>
                    <div className="col-lg-6 col-md-6 col-sm-6">
                      <span className="mx-4">
                        <a href="#" data-toggle="modal" data-target="#reports" onClick={ (e)=>props.selectReport(e,props.graphConfig.id,'graph','custom') } >Add to Report</a>
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
              return <div className="col-lg-4 col-sm-12" key={i}>
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
      url: 'analytics/api/update-graph-config/'
    }

    this.handleCheckboxInputChanged = this.handleCheckboxInputChanged.bind(this)
    this.setDashboard = this.setDashboard.bind(this)
    this.selectReport = this.selectReport.bind(this)
    this.editGraph = this.editGraph.bind(this)
	}


  handleCheckboxInputChanged(e, id){
    console.log("value is ")
    console.log(id)
    console.log(e.target.checked)

    this.setDashboard(e.target.checked, id)
  }

  selectReport(e,id_,cat,table_type){
        console.log("value is ")
        console.log(id_)

        // var mod_val = document.getElementById('module_name')
        // var report_type = document.getElementById('report_type')
        // mod_val.value = val
        // report_type.value = type

        var report_cat = document.getElementById('report_cat')
        var report_table_type = document.getElementById('report_table_type')
        var report_id = document.getElementById('report_id')
        report_cat.value = cat
        report_table_type.value = table_type
        report_id.value = id_

        // console.log(mod_val.value)
    }

  editGraph(e, graphConfig){
    // console.log("graph config is ")
    // console.log(graphConfig)

    // set graph config id
    var graphConfig_id = document.querySelector(".graphConfig")
    graphConfig_id.value = graphConfig.id

    console.log("giving them ID ")
    console.log(graphConfig_id.value)


    // Set predictive check
    var predictive = document.querySelector(".predictive")
    predictive.checked = graphConfig.predictive

    // Set predictive Balance
    var predictive_balance = document.querySelector(".predictive_balance")
    predictive_balance.value = graphConfig.predictive_balance

    document.querySelector(".predictive_range_value").innerHTML = graphConfig.predictive_balance

    // Set predictive added values
    var predictive_added_values = document.querySelector(".predictive_added_values")
    predictive_added_values.value = graphConfig.predictive_to

    document.querySelector(".predictive_added_value").innerHTML = graphConfig.predictive_to

    // Set show on dashboard
    var show_on_dashboard = document.querySelector(".show_on_dashboard")
    show_on_dashboard.checked = graphConfig.on_dashboard



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
                  this.props.data.Graph_config.filter(config=>((this.props.view=="dashboard" && config.on_dashboard==1) || (this.props.view=="graph" && this.props.graphid=="all") || (this.props.view=="graph" && this.props.graphid==config.id))).map((graph,i)=>{
                    // console.log("Module selected is ")
                    // console.log(this.props.graphid)
                    // console.log(config.id)
                    return <React.Fragment key={i}>
                    {
                      this.props.data.modules ?
                      this.props.data.modules.filter(module=>(module.id==graph.module && this.props.module=="all") || (module.id==graph.module && module.module_name==this.props.module)).map((module,r)=>{
                        // console.log("Singular module is ")
                        // console.log(module.module_name)
                        // console.log(this.props.data)
                        return <ColumnMaker key={r} data={ this.props.data } module={ module } graphConfig={ graph } handleCheckboxInputChanged={ this.handleCheckboxInputChanged } view={this.props.view} selectReport={ this.selectReport } editGraph={ this.editGraph }/>
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