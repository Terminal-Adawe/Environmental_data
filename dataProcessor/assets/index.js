import React from 'react';
import ReactDOM from 'react-dom';
import Form from './forms';
import LoadingOverlay from 'react-loading-overlay';


class Index extends React.Component {
	constructor(){
		super()

		this.state={
			loader: false,
		}

	}


	render(){
		return (<LoadingOverlay
  					active={this.state.loader}
  					spinner
  					text='Loading your content...'
  				>
				<Form loader={ this.toggleLoader } />
  			</LoadingOverlay>)
	}
}

export default Index

if (document.getElementById('form')) {
    ReactDOM.render(<Form />, document.getElementById('form'));
}