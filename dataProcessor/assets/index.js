import React from 'react';
import ReactDOM from 'react-dom';
import Form from './forms';


class Index extends React.Component {
	constructor(){
		super()

	}


	render(){
		return (<React.Fragment>
				<Form />
  			</React.Fragment>)
	}
}

export default Index

if (document.getElementById('form')) {
    ReactDOM.render(<Index />, document.getElementById('form'));
}