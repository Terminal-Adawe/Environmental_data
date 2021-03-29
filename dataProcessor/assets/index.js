import React from 'react';
import ReactDOM from 'react-dom';
import Form from './forms';
import LoadingOverlay from 'react-loading-overlay';


class Index extends React.Component {
	constructor(){
		super()

		this.state={
			loader: false,
			baseUrl: "http://3.9.132.4",
		}

		this.toggleLoader = this.toggleLoader.bind(this)
	}

	toggleLoader(state){
    	console.log('loader is '+state)

    	this.setState({
    		loader: state
    	})
    }


	render(){
		return (<LoadingOverlay
  					active={this.state.loader}
  					spinner
  					text='Loading...'
  				>
				<Form loader={ this.toggleLoader } baseUrl={ this.state.baseUrl } />
  			</LoadingOverlay>)
	}
}

export default Index

if (document.getElementById('form')) {
    ReactDOM.render(<Index />, document.getElementById('form'));
}