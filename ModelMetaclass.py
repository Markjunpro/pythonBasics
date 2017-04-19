class ModelMetaclass(type):
    
    def __new__(clsmname,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        tableName = attrs.get('__table__',None) or name
        logging.info)'found model :%s (table :%s)' % (name,tableName))
        mappings = dict()
        fields =[]
        primaryKey =None
        for k , v in attrs.items():
            if isinstance(v,Field ):
                logging.info( '   found mapping :%s ==> %s ' % (k,v))
                mappings[k] =v 
                if v.primary_key:
                    if primaryKey:
                        raise RuntimrError('Duplicate primary key for field: %s ' % k)
                    primaryKey=k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError('Primary key not found')
        for k in mappings.key():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: ''%s'' % f, fields))
        attrs['__mapings__'] =mappings
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey
        attrs['__fields__'] =fields
        attrs['__select__'] = 'select '%s',%s from '%s'' % (primaryKey,','.join(escaped_fields),tableName)
        attrs'__init__'] = 'insert into '%s' (%s,'%s') values (%s)' % (tableName,','.joi(map(lambda f ''%s'=?' % (mapping.get(f).name or f),fields)),primaryKey)
        attrs['__updata__']= 'updata '%s' (%s,'%s') values (%s)'  % (tablesName,','.join(map(lambda f : ''%s'=?' % (mappings.get(f).name or f),fields)),primaryKey)
        attrs['__delete__'] = 'delete from '%s' where '%s' =?' % (tableName,primaryKey)
        return type.__new__(cls,name,bases,attrs)
