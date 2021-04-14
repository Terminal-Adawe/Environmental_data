import React from 'react';
import ReactDOM from "react-dom";
import Widgets_custom from './widget_custom';
import Widgets_a from './widget1';
import Widgets_b from './widget2';
import Widgets_c from './widget3';
import FormulateGraphData from './formulateGraphData';

function ColumnMaker(props){
	
	// console.log("Props are ")
	// console.log(props.data.Storage_facility)
	// console.log(props)

	
  let data = ""
  let module_name = ""

  props.data ? data = props.data : data = ""
  props.module.descriptions ? module_name=props.module.description : ""

  console.log("module name is "+props.module.description)
									
		return (<div className="col-lg-6 col-sm-12 mt-3">
              <FormulateGraphData data={data} module={props.module} graphConfig={ props.graphConfig }/>
            </div>)
									
								
	}


function Widget_generator(props){
  return (<React.Fragment>
          {
            props.widgets.map((widget,i)=>{
              console.log('widget 1 ')
              console.log(widget)
          //   props.data ? 
              return <Widgets_custom compliance={ props.data.ComplianceValue } parameter={ widget[0] } background={ widget[1] } />
          //   : ""
            })
          }
       </React.Fragment>)

      // return <React.Fragment>
      //           <Widgets_a compliance={ props.data.ComplianceValue } parameter={ props.parameter } />
      //           <Widgets_b compliance={ props.data.ComplianceValue } parameter={ props.parameter } />
      //           <Widgets_c compliance={ props.data.ComplianceValue } parameter={ props.parameter } />
      //       </React.Fragment>
} 



class Template extends React.Component {
	constructor(){
		super()

    this.state={
      widget1: "Turbidity",
      widget2: "Chemical Oxygen Demand",
      widget3: "Total Arsenic",
      widgets: [["Turbidity","#17c1f3"],["Chemical Oxygen Demand","#f0be08"],["Total Arsenic","#bb8fce"]],
    }

	}


  


	render(){
		return (<div className="row">
					<div className="col-12">
						<div className="row">
              {
                this.props.module=="all" ? <Widget_generator data={ this.props.data } widgets={ this.state.widgets } module={ this.props.module } parameter={ this.state.widget1 } /> : ""
              }
                      
								
                {
                  this.props.data.Graph_config ? 
                  this.props.data.Graph_config.map((graph,i)=>{
                    return <React.Fragment key={i}>
                    {
                      this.props.data.modules ?
                      this.props.data.modules.filter(module=>(module.id==graph.module && this.props.module=="all") || (module.id==graph.module && module.module_name==this.props.module)).map((module,i)=>{
                        return <ColumnMaker key={i} data={ this.props.data } module={ module } graphConfig={ graph }/>
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