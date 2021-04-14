import React from 'react';
import ReactDOM from 'react-dom';
import Form from './forms';
import LoadingOverlay from 'react-loading-overlay';


class Index extends React.Component {
	constructor(){
		super()

		this.state={
			loader: false,
			baseUrl: "https://d12m8zkkfoc9oy.cloudfront.net",
			// baseUrl: "http://localhost:8002",
			location: [],
		}

		this.toggleLoader = this.toggleLoader.bind(this)
		this.getLocation = this.getLocation.bind(this)
		this.showPosition = this.showPosition.bind(this)
	}

	componentDidMount(){
		this.getLocation()

		const baseUrl = document.getElementById("baseUrl").value

		this.setState({
			baseUrl: baseUrl
		},()=>{

		})

	}

	toggleLoader(state){
    	this.setState({
    		loader: state
    	})
    }

    getLocation(){
    	if (navigator.geolocation) {
    		navigator.geolocation.getCurrentPosition(this.showPosition);
  		} else {

  		}
    }

    showPosition(position){
    	var data = position.coords.latitude+","+position.coords.longitude

    	console.log("Geo location is ")
    	console.log(data)

    	this.setState({
    		location: data
    	})
    }


	render(){
		return (<LoadingOverlay
  					active={this.state.loader}
  					spinner
  					text='Uploading Data...'
  				>
				<Form loader={ this.toggleLoader } baseUrl={ this.state.baseUrl } getLocation={ this.getLocation } location={ this.state.location } />
  			</LoadingOverlay>)
	}
}

export default Index

if (document.getElementById('form')) {
    ReactDOM.render(<Index />, document.getElementById('form'));
}