import { CompactTable } from '@table-library/react-table-library/compact';
import { useTheme } from '@table-library/react-table-library/theme';
import { getTheme } from '@table-library/react-table-library/baseline';


export function Table({nodes}){
    let COLUMNS = []
    let isDataEmpty = false
    if(nodes === undefined && nodes === null){
      isDataEmpty = true
    }

    COLUMNS = isDataEmpty? []:
      Object.keys(nodes[0]).map((key) => ({
        label: key,
        renderCell: ((item) => item[key])
      }));
    
    return (
      <div className='amortization-table'>
        <CompactTable columns={COLUMNS} data={{nodes}} theme={useTheme(getTheme())} 
        />;
      </div>
    )
};