import React from 'react'
import Highlight, {defaultProps} from 'prism-react-renderer'

class texto extends Component {
    constructor(props){
        super(props);
        this.children = props.children
    }
    render() { 
        return ( 
            <Highlight {...defaultProps} code={this.children} language="javascript">
      {({className, style, tokens, getLineProps, getTokenProps}) => (
        <pre className={className} style={{...style, padding: '20px'}}>
          {tokens.map((line, i) => (
            <div key={i} {...getLineProps({line, key: i})}>
              {line.map((token, key) => (
                <span key={key} {...getTokenProps({token, key})} />
              ))}
            </div>
          ))}
        </pre>
      )}
    </Highlight>
         );
    }
}
export default texto;