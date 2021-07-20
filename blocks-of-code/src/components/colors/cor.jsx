import React, { Component } from 'react';

class cor extends Component {
    constructor(props){
        this.color = this.props.color;
        this.arrayTags = this.props.children;
    }

    render() { 
        return ( 
            <span 
                style={"color:${color}"}
            >
                {arrayTags}
            </span>
         );
    }
}
export default cor;