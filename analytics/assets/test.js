import React from 'react';
import ReactDOM from "react-dom";
import BarGraph from './bargraph';
import LineGraph from './linegraph';

import axios from "axios";
import cookie from "react-cookies";


class Test extends React.Component {
	constructor(){
		super()

		this.state={
			data: [],
            username: "",
            module: "",
            x_column: "",
            y_column: "",
            baseUrl: "",
            valueType: "",
            table_name: "",
            url: "add/build-table/",
		}

        this.getReport = this.getReport.bind(this)

	}

	componentDidMount(){
			// console.log("processing graph ... ")
			// console.log(this.props)
            const baseUrl = document.getElementById("baseUrl").value

            this.setState({
                baseUrl: baseUrl,
                module_name: this.props.module_name,
                x_column: this.props.x_column,
                y_column: this.props.y_column,
                valueType: this.props.valueType,
                groupType: this.props.groupType,
                table_name: this.props.table_name,
                username: this.props.username

            },()=>{
                console.log("Params are "+this.props.module_name+" ++ "+this.props.x_column+" ++ "+this.props.y_column+" ++ "+this.props.valueType+" ++ "+this.props.groupType)
                if(this.props.module_name != ""){
                    this.getReport(this.props.username,this.props.table_name,this.props.module_name,this.props.x_column,this.props.y_column,this.props.valueType, this.props.groupType)
                } 
            })


             // this.props.data ? 
             // data = this.formulateGraph(this.props.graphData)
             // : data = []

    		// console.log("manipulated data is ")
    		// console.log(data)

	}

	componentDidUpdate(prevProps, prevState){
		if(prevProps.module_name != this.props.module_name || prevProps.x_column != this.props.x_column || prevProps.y_column != this.props.y_column || prevProps.valueType != this.props.valueType){
			// console.log("processing graph 2... ")
			// console.log(this.props)
			this.getReport(this.props.username,this.props.table_name,this.props.module_name,this.props.x_column,this.props.y_column,this.props.valueType, this.props.groupType)
		}

        if(prevProps.groupType != this.props.groupType){
            
        }
	}

    getReport(username,table_name,module_, x_column, y_column, valueType, groupType){
        let form_data = new FormData();

        const url = this.state.url
        const baseUrl = this.state.baseUrl


        console.log("sending info ... ")
        console.log(module_+" + "+x_column+" + "+y_column+" + "+valueType+" + "+groupType)
        console.log("Base url is ")
        console.log(this.state.baseUrl)

        form_data.append('username', username)
        form_data.append('table_name', table_name)
        form_data.append('module', module_)
        form_data.append('x_column', x_column)
        form_data.append('y_column', y_column)
        form_data.append('value', valueType)
        form_data.append('groupType', groupType)

        axios.post(`${baseUrl}/api/${url}`,form_data,{
                headers: {
                     'X-CSRFTOKEN': cookie.load("csrftoken"),
                 },
            }
            )
      .then(response => {
        console.log("Response generated is ")
        console.log(response.data)
        // this.props.loader(false)

        response.data.map((resp,i)=>{
            console.log(resp)
        })

        // Response is successful
        if(response.status == "201"){
            console.log(response.statusText)

            // window.scrollTo({top: 0, behavior: 'smooth'});
            
            // var inputs = document.querySelectorAll('.input-element')
            // let count_p = 0 
            // let count_d = 0
            
            //  console.log("Set everything to empty")
            // // Set everythinng to empty
            // inputs.forEach((input,i)=>{
              
            //         input.value = ""
                
            // })

            // this.props.getData(response.data)

            this.setState({
                data: response.data
            })

            setTimeout(function(){
                document.getElementById('success-message').innerHTML = ""
            },4000)

        } else // response failed
        {
            document.getElementById('error-message').innerHTML = response.data.message
            console.log(response.data.message)
            setTimeout(function(){
               document.getElementById('error-message').innerHTML = ""
            },10000)
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
            let columns = []
            let rows = []

			return (<div className="container-fluid">
                        <div className="table-responsive">          
                            <table className="table table-bordered table-striped">
                              {
                                this.state.data.map((main_row,i)=>{
                                    if(i==0){
                                        return <thead key={i}><tr>
                                                <th></th>
                                                {
                                                    this.state.data.map((row,r)=>{
                                                        let trigger = 0;
                                                        for(var r = 0; r < columns.length; r++){
                                                            if(columns[r]==row.column){
                                                                trigger = 1;
                
                                                                break;
                                                            }
                                                        }
                                                        
                
                                                        if (trigger == 0){
                                                            columns = [...columns, row.column]
                                                            if(row.column){
                                                                return <th key={i}>{ row.column }</th>
                                                            } else {
                                                                return null
                                                            }
                                                        }
                                                        })
                                                }
                                            </tr></thead>
                                    } else {
                                        let trigger = 0;

                                        for(var r = 0; r < rows.length; r++){
                                            if(rows[r]==main_row.row){
                                                trigger = 1;

                                                break;
                                            }
                                        }

                                        if (trigger == 0){
                                        rows = [...rows, main_row.row]
                                        return <tr key={r}>
                                                <th>{ main_row.row }</th>
                                                {   
                                                    
                                                        this.state.data.map((row,i)=>{
                                                            if(main_row.column && main_row.row){
                                                                if(row.column == columns[i] && row.row == main_row.row){
                                                                    return <th key={i}>{ row.value }</th>
                                                                } else {
                                                                    return <th key={i}></th>
                                                                }
                                                            } else if (main_row.column && !main_row.row){
                                    
                                                                    return <th key={i}>{ row.value }</th>
    
                                                            } else {
                                                                return <th key={i}></th>
                                                            }
                                                        })
                                                    
                                                }
                                            </tr>
                                        }
                                    }
                                })
                              }
                            </table>
                        </div>
                        </div>)
		}
		
	
}

export default Test


