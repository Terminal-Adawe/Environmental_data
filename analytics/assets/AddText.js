import React from 'react';
import ReactDOM from "react-dom";

import axios from "axios";
import cookie from "react-cookies";


function AddText(props){
	return (<React.Fragment>
		<p>
  <button className="btn btn-primary" type="button" data-toggle="collapse" data-target={`#collapse${props.position}${props.positionid}`} aria-expanded="false" aria-controls="collapseExample">
    Add Note {props.position} representation
  </button>
</p>
<div className="collapse" id={`collapse${props.position}${props.positionid}`}>
  <div className="card card-body">
    <textarea className="form-control" id="exampleFormControlTextarea1" rows="3" onChange={ (e)=>props.textAreaChangeFunc(e,props.position, props.positionid) }></textarea>
  </div>
</div>
</React.Fragment>)
}

export default AddText;
