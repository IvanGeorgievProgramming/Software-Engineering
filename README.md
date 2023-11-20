# cProfile

## Main
```bash
         45923 function calls (45006 primitive calls) in 0.040 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      120    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(concatenate)
      183    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(copyto)
       20    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(prod)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:262(__subclasshook__)
        5    0.000    0.000    0.000    0.000 <frozen _collections_abc>:283(__subclasshook__)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:362(__subclasshook__)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:381(__subclasshook__)
       13    0.000    0.000    0.000    0.000 <frozen _collections_abc>:409(__subclasshook__)
        5    0.000    0.000    0.000    0.000 <frozen _collections_abc>:78(_check_methods)
      357    0.000    0.000    0.000    0.000 <frozen abc>:117(__instancecheck__)
    50/11    0.000    0.000    0.000    0.000 <frozen abc>:121(__subclasscheck__)
       24    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
       24    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
       72    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
       72    0.000    0.000    0.000    0.000 <frozen codecs>:331(getstate)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:100(acquire)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1028(__enter__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1032(__exit__)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1056(_find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1103(_sanity_check)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1122(_find_and_load_unlocked)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1167(_find_and_load)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1194(_gcd_import)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:125(release)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:165(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:169(__enter__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:173(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:179(_get_module_lock)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:198(cb)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:233(_call_with_frames_removed)
       45    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:244(_verbose_message)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:357(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:71(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:748(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:922(find_spec)
       45    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:119(<listcomp>)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:140(_path_stat)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1421(_path_importer_cache)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:1464(_get_spec)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap_external>:1496(find_spec)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1604(find_spec)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:67(_relax_case)
       45    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:96(_path_join)
       72    0.000    0.000    0.000    0.000 <frozen ntpath>:319(expanduser)
        1    0.000    0.000    0.000    0.000 <frozen os>:1081(__subclasshook__)
       24    0.000    0.000    0.000    0.000 <string>:1(<lambda>)
        1    0.000    0.000    0.040    0.040 <string>:1(<module>)
       24    0.000    0.000    0.000    0.000 <string>:2(__init__)
        1    0.000    0.000    0.001    0.001 __init__.py:108(import_module)
       87    0.000    0.000    0.000    0.000 __init__.py:33(using_copy_on_write)
      111    0.000    0.000    0.000    0.000 __init__.py:43(using_pyarrow_string_dtype)
        1    0.000    0.000    0.000    0.000 __init__.py:89(find_spec)
        1    0.000    0.000    0.000    0.000 __init__.py:96(<lambda>)
       48    0.000    0.000    0.000    0.000 _asarray.py:112(<setcomp>)
       48    0.000    0.000    0.000    0.000 _asarray.py:31(require)
        2    0.000    0.000    0.000    0.000 _dtype.py:24(_kind_name)
        2    0.000    0.000    0.000    0.000 _dtype.py:330(_name_includes_bit_suffix)
        2    0.000    0.000    0.000    0.000 _dtype.py:344(_name_get)
       15    0.000    0.000    0.000    0.000 _methods.py:39(_amax)
       20    0.000    0.000    0.000    0.000 _methods.py:47(_sum)
       54    0.000    0.000    0.000    0.000 _methods.py:55(_any)
        1    0.000    0.000    0.001    0.001 _optional.py:81(import_optional_dependency)
       59    0.000    0.000    0.000    0.000 _validators.py:226(validate_bool_kwarg)
       24    0.000    0.000    0.000    0.000 _validators.py:450(check_dtype_backend)
        2    0.000    0.000    0.000    0.000 arrayprint.py:1571(_array_str_implementation)
       18    0.000    0.000    0.000    0.000 arrayprint.py:389(_object_format)
        2    0.000    0.000    0.000    0.000 arrayprint.py:403(_get_formatdict)
        2    0.000    0.000    0.000    0.000 arrayprint.py:421(<lambda>)
        2    0.000    0.000    0.000    0.000 arrayprint.py:452(_get_format_function)
        2    0.000    0.000    0.000    0.000 arrayprint.py:506(wrapper)
        2    0.000    0.000    0.000    0.000 arrayprint.py:523(_array2string)
        2    0.000    0.000    0.000    0.000 arrayprint.py:561(array2string)
        2    0.000    0.000    0.000    0.000 arrayprint.py:64(_make_options_dict)
        2    0.000    0.000    0.000    0.000 arrayprint.py:72(<dictcomp>)
       18    0.000    0.000    0.000    0.000 arrayprint.py:739(_extendLine)
       18    0.000    0.000    0.000    0.000 arrayprint.py:753(_extendLine_pretty)
        2    0.000    0.000    0.000    0.000 arrayprint.py:780(_formatArray)
     20/2    0.000    0.000    0.000    0.000 arrayprint.py:789(recurser)
       48    0.000    0.000    0.000    0.000 base.py:1656(name)
       22    0.000    0.000    0.000    0.000 base.py:2292(is_unique)
       52    0.000    0.000    0.000    0.000 base.py:3762(get_loc)
       37    0.000    0.000    0.000    0.000 base.py:458(_engine_type)
       87    0.001    0.000    0.005    0.000 base.py:477(__new__)
        2    0.000    0.000    0.000    0.000 base.py:5070(values)
       24    0.000    0.000    0.000    0.000 base.py:510(find)
      183    0.000    0.000    0.000    0.000 base.py:5126(_values)
       37    0.000    0.000    0.000    0.000 base.py:5152(_get_engine_target)
       57    0.000    0.000    0.001    0.000 base.py:5299(__contains__)
       76    0.000    0.000    0.000    0.000 base.py:5349(__getitem__)
       48    0.000    0.000    0.000    0.000 base.py:538(<genexpr>)
        2    0.000    0.000    0.000    0.000 base.py:5391(_getitem_slice)
       24    0.000    0.000    0.001    0.000 base.py:5518(equals)
       24    0.000    0.000    0.001    0.000 base.py:5609(identical)
       48    0.000    0.000    0.000    0.000 base.py:5634(<genexpr>)
       87    0.000    0.000    0.000    0.000 base.py:573(_ensure_array)
       87    0.000    0.000    0.000    0.000 base.py:591(_dtype_to_subclass)
       39    0.000    0.000    0.000    0.000 base.py:61(__len__)
      104    0.000    0.000    0.000    0.000 base.py:648(_simple_new)
       52    0.000    0.000    0.000    0.000 base.py:6611(_maybe_cast_indexer)
       52    0.000    0.000    0.000    0.000 base.py:69(shape)
       15    0.000    0.000    0.000    0.000 base.py:691(_constructor)
      156    0.000    0.000    0.000    0.000 base.py:71(<genexpr>)
       87    0.000    0.000    0.000    0.000 base.py:73(_validate_set_axis)
       15    0.000    0.000    0.001    0.000 base.py:7472(ensure_index_from_sequences)
      255    0.000    0.000    0.004    0.000 base.py:7512(ensure_index)
      183    0.000    0.000    0.000    0.000 base.py:7607(maybe_extract_name)
       24    0.000    0.000    0.000    0.000 base.py:790(is_)
      128    0.000    0.000    0.000    0.000 base.py:830(_reset_identity)
       24    0.000    0.000    0.000    0.000 base.py:836(__iter__)
       15    0.000    0.000    0.000    0.000 base.py:837(_cleanup)
       37    0.000    0.000    0.001    0.000 base.py:841(_engine)
      418    0.000    0.000    0.000    0.000 base.py:908(__len__)
       85    0.000    0.000    0.000    0.000 base.py:973(dtype)
       24    0.000    0.000    0.000    0.000 base_parser.py:1113(_make_date_converter)
       24    0.000    0.000    0.000    0.000 base_parser.py:114(__init__)
       24    0.000    0.000    0.000    0.000 base_parser.py:1247(_process_date_conversion)
       24    0.000    0.000    0.000    0.000 base_parser.py:1404(_validate_parse_dates_arg)
       72    0.000    0.000    0.000    0.000 base_parser.py:1425(is_index_col)
       24    0.000    0.000    0.000    0.000 base_parser.py:190(_validate_parse_dates_presence)
       24    0.000    0.000    0.000    0.000 base_parser.py:234(<setcomp>)
       24    0.000    0.000    0.000    0.000 base_parser.py:246(<listcomp>)
       24    0.000    0.000    0.000    0.000 base_parser.py:254(_has_complex_date_col)
       24    0.000    0.000    0.000    0.000 base_parser.py:278(_extract_multi_indexer_columns)
       24    0.000    0.000    0.000    0.000 base_parser.py:349(_maybe_make_multi_index_columns)
       24    0.000    0.000    0.000    0.000 base_parser.py:361(_make_index)
       24    0.000    0.000    0.000    0.000 base_parser.py:600(_set_noconvert_dtype_columns)
       24    0.000    0.000    0.000    0.000 base_parser.py:861(_do_date_conversions)
       24    0.000    0.000    0.000    0.000 base_parser.py:883(_check_data_length)
       24    0.000    0.000    0.000    0.000 base_parser.py:976(_validate_usecols_arg)
       37    0.000    0.000    0.000    0.000 blocks.py:1007(iget)
       15    0.000    0.000    0.000    0.000 blocks.py:1016(_slice)
       48    0.000    0.000    0.000    0.000 blocks.py:187(is_extension)
       48    0.000    0.000    0.000    0.000 blocks.py:192(_can_consolidate)
        2    0.000    0.000    0.000    0.000 blocks.py:222(external_values)
       15    0.000    0.000    0.000    0.000 blocks.py:2236(is_view)
       48    0.000    0.000    0.000    0.000 blocks.py:2317(maybe_coerce_values)
      111    0.000    0.000    0.000    0.000 blocks.py:2346(get_block_type)
       63    0.000    0.000    0.000    0.000 blocks.py:2388(new_block)
       24    0.000    0.000    0.000    0.000 blocks.py:2467(extend_blocks)
        2    0.000    0.000    0.000    0.000 blocks.py:2586(external_values)
       15    0.000    0.000    0.000    0.000 blocks.py:323(getitem_block_columns)
       63    0.000    0.000    0.000    0.000 blocks.py:583(dtype)
       24    0.000    0.000    0.000    0.000 blocks.py:639(copy)
       24    0.000    0.000    0.000    0.000 c_parser_wrapper.py:194(close)
       24    0.000    0.000    0.000    0.000 c_parser_wrapper.py:201(_set_noconvert_columns)
       24    0.000    0.000    0.000    0.000 c_parser_wrapper.py:212(<dictcomp>)
       24    0.000    0.000    0.000    0.000 c_parser_wrapper.py:213(<listcomp>)
       24    0.000    0.000    0.003    0.000 c_parser_wrapper.py:222(read)
       24    0.000    0.000    0.000    0.000 c_parser_wrapper.py:326(<listcomp>)
       24    0.000    0.000    0.000    0.000 c_parser_wrapper.py:330(<dictcomp>)
       24    0.000    0.000    0.001    0.000 c_parser_wrapper.py:355(_concatenate_chunks)
      120    0.000    0.000    0.000    0.000 c_parser_wrapper.py:367(<listcomp>)
      120    0.000    0.000    0.000    0.000 c_parser_wrapper.py:369(<setcomp>)
      120    0.000    0.000    0.000    0.000 c_parser_wrapper.py:370(<setcomp>)
       24    0.000    0.000    0.000    0.000 c_parser_wrapper.py:392(ensure_dtype_objs)
       24    0.002    0.000    0.003    0.000 c_parser_wrapper.py:60(__init__)
      111    0.000    0.000    0.001    0.000 cast.py:1147(maybe_infer_to_datetimelike)
       72    0.000    0.000    0.001    0.000 cast.py:119(maybe_convert_platform)
       96    0.000    0.000    0.000    0.000 cast.py:1544(construct_1d_object_array_from_listlike)
       37    0.000    0.000    0.000    0.000 common.py:1025(needs_i8_conversion)
       24    0.000    0.000    0.000    0.000 common.py:1107(_maybe_memory_map)
       48    0.000    0.000    0.001    0.000 common.py:1155(_is_binary_mode)
        1    0.000    0.000    0.001    0.001 common.py:1176(_get_binary_io_classes)
       15    0.000    0.000    0.000    0.000 common.py:1183(is_bool_dtype)
       48    0.000    0.000    0.000    0.000 common.py:1194(is_potential_multi_index)
       48    0.000    0.000    0.000    0.000 common.py:121(classes)
       24    0.000    0.000    0.001    0.000 common.py:121(close)
       96    0.000    0.000    0.000    0.000 common.py:1219(<genexpr>)
       24    0.000    0.000    0.000    0.000 common.py:1223(dedup_names)
       48    0.000    0.000    0.000    0.000 common.py:123(<lambda>)
      120    0.000    0.000    0.000    0.000 common.py:1255(is_1d_only_ea_dtype)
      174    0.000    0.000    0.000    0.000 common.py:1322(is_ea_or_datetimelike_dtype)
       48    0.000    0.000    0.000    0.000 common.py:137(is_object_dtype)
       15    0.000    0.000    0.000    0.000 common.py:1390(_get_dtype)
       48    0.000    0.000    0.000    0.000 common.py:1425(_is_dtype_type)
       24    0.000    0.000    0.000    0.000 common.py:145(is_url)
       59    0.000    0.000    0.000    0.000 common.py:149(cast_scalar_indexer)
       72    0.000    0.000    0.000    0.000 common.py:1562(validate_all_hashable)
      144    0.000    0.000    0.000    0.000 common.py:1581(<genexpr>)
       48    0.000    0.000    0.000    0.000 common.py:1587(pandas_dtype)
       72    0.000    0.000    0.000    0.000 common.py:173(_expand_user)
       24    0.000    0.000    0.000    0.000 common.py:185(all_none)
       48    0.000    0.000    0.000    0.000 common.py:189(<genexpr>)
       24    0.000    0.000    0.000    0.000 common.py:192(validate_header_arg)
       15    0.000    0.000    0.000    0.000 common.py:228(asarray_tuplesafe)
       48    0.000    0.000    0.000    0.000 common.py:233(stringify_path)
       24    0.000    0.000    0.000    0.000 common.py:277(is_fsspec_url)
       24    0.000    0.000    0.001    0.000 common.py:289(_get_filepath_or_buffer)
       24    0.000    0.000    0.000    0.000 common.py:296(maybe_iterable_to_list)
       37    0.000    0.000    0.000    0.000 common.py:367(apply_if_callable)
       24    0.000    0.000    0.000    0.000 common.py:503(get_compression_method)
       24    0.000    0.000    0.000    0.000 common.py:514(is_string_or_object_np_dtype)
       24    0.000    0.000    0.000    0.000 common.py:538(infer_compression)
      168    0.000    0.000    0.000    0.000 common.py:556(require_length_match)
       24    0.000    0.000    0.004    0.000 common.py:652(get_handle)
       48    0.000    0.000    0.000    0.000 common.py:91(ensure_python_int)
       30    0.000    0.000    0.000    0.000 common.py:96(is_bool_indexer)
      120    0.000    0.000    0.001    0.000 concat.py:52(concat_compat)
      120    0.000    0.000    0.000    0.000 concat.py:73(<listcomp>)
       72    0.000    0.000    0.000    0.000 config.py:127(_get_single_key)
       72    0.000    0.000    0.000    0.000 config.py:145(_get_option)
       72    0.000    0.000    0.001    0.000 config.py:271(__call__)
       72    0.000    0.000    0.000    0.000 config.py:615(_select_options)
       72    0.000    0.000    0.000    0.000 config.py:633(_get_root)
      144    0.000    0.000    0.000    0.000 config.py:647(_get_deprecated_option)
       72    0.000    0.000    0.000    0.000 config.py:674(_translate_key)
       72    0.000    0.000    0.000    0.000 config.py:686(_warn_if_deprecated)
       24    0.000    0.000    0.000    0.000 construction.py:196(mgr_to_mgr)
      255    0.000    0.000    0.000    0.000 construction.py:419(extract_array)
       24    0.000    0.000    0.014    0.001 construction.py:423(dict_to_mgr)
      135    0.000    0.000    0.000    0.000 construction.py:484(ensure_wrapped_if_datetimelike)
       24    0.000    0.000    0.000    0.000 construction.py:487(<listcomp>)
      255    0.001    0.000    0.004    0.000 construction.py:518(sanitize_array)
       24    0.000    0.000    0.001    0.000 construction.py:596(_homogenize)
       96    0.000    0.000    0.000    0.000 construction.py:665(_sanitize_non_ordered)
      255    0.000    0.000    0.000    0.000 construction.py:673(_sanitize_ndim)
      255    0.000    0.000    0.000    0.000 construction.py:712(_sanitize_str_dtypes)
      255    0.000    0.000    0.000    0.000 construction.py:732(_maybe_repeat)
       24    0.000    0.000    0.000    0.000 construction.py:743(_try_cast)
       24    0.000    0.000    0.003    0.000 construction.py:96(arrays_to_mgr)
       24    0.000    0.000    0.000    0.000 copy.py:107(_copy_immutable)
       24    0.000    0.000    0.000    0.000 copy.py:66(copy)
       24    0.000    0.000    0.000    0.000 enum.py:1248(value)
       24    0.000    0.000    0.000    0.000 enum.py:192(__get__)
      157    0.000    0.000    0.000    0.000 flags.py:53(__init__)
      100    0.000    0.000    0.000    0.000 flags.py:57(allows_duplicate_labels)
       85    0.000    0.000    0.000    0.000 flags.py:89(allows_duplicate_labels)
       15    0.000    0.000    0.000    0.000 frame.py:1542(__len__)
       22    0.000    0.000    0.001    0.000 frame.py:3779(_ixs)
       22    0.000    0.000    0.001    0.000 frame.py:3856(__getitem__)
       22    0.000    0.000    0.000    0.000 frame.py:4387(_box_col_values)
       15    0.000    0.000    0.000    0.000 frame.py:4402(_clear_item_cache)
       22    0.000    0.000    0.001    0.000 frame.py:4405(_get_item_cache)
       15    0.000    0.000    0.005    0.000 frame.py:5744(set_index)
       37    0.000    0.000    0.000    0.000 frame.py:653(_sliced_from_mgr)
       37    0.000    0.000    0.000    0.000 frame.py:656(_constructor_sliced_from_mgr)
       24    0.000    0.000    0.014    0.001 frame.py:668(__init__)
       15    0.000    0.000    0.000    0.000 frame.py:952(axes)
       20    0.000    0.000    0.000    0.000 fromnumeric.py:2950(_prod_dispatcher)
       20    0.000    0.000    0.000    0.000 fromnumeric.py:2955(prod)
       20    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
       20    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
       20    0.000    0.000    0.000    0.000 function.py:411(validate_func)
       44    0.000    0.000    0.000    0.000 function.py:64(__call__)
        2    0.000    0.000    0.003    0.001 functions.py:11(get_all_student_names)
        5    0.000    0.000    0.006    0.001 functions.py:18(calculate_average_mark_for_test)
       15    0.000    0.000    0.023    0.002 functions.py:29(calculate_average_mark_for_student)
        1    0.000    0.000    0.007    0.007 functions.py:44(get_all_tests_average_marks)
        1    0.000    0.000    0.023    0.023 functions.py:52(get_all_failed_students)
        2    0.000    0.000    0.004    0.002 functions.py:6(get_all_test_names)
       20    0.000    0.000    0.001    0.000 generic.py:11920(_stat_function)
       20    0.000    0.000    0.001    0.000 generic.py:11971(mean)
      157    0.000    0.000    0.000    0.000 generic.py:274(__init__)
       61    0.000    0.000    0.000    0.000 generic.py:335(_from_mgr)
       85    0.000    0.000    0.000    0.000 generic.py:358(attrs)
     1134    0.000    0.000    0.000    0.000 generic.py:37(_check)
      185    0.000    0.000    0.000    0.000 generic.py:393(flags)
       15    0.000    0.000    0.001    0.000 generic.py:4094(xs)
     1134    0.000    0.000    0.001    0.000 generic.py:42(_instancecheck)
       15    0.000    0.000    0.000    0.000 generic.py:4314(_set_is_copy)
       15    0.000    0.000    0.002    0.000 generic.py:4412(__delitem__)
       15    0.000    0.000    0.000    0.000 generic.py:4453(_check_inplace_and_allows_duplicate_labels)
       15    0.000    0.000    0.000    0.000 generic.py:4520(_is_view)
       48    0.000    0.000    0.000    0.000 generic.py:487(_validate_dtype)
       24    0.000    0.000    0.002    0.000 generic.py:5266(reindex)
      128    0.000    0.000    0.000    0.000 generic.py:548(_get_axis_number)
       48    0.000    0.000    0.001    0.000 generic.py:5509(<genexpr>)
       69    0.000    0.000    0.000    0.000 generic.py:562(_get_axis)
       85    0.000    0.000    0.000    0.000 generic.py:6147(__finalize__)
      102    0.000    0.000    0.000    0.000 generic.py:6189(__getattr__)
      259    0.000    0.000    0.001    0.000 generic.py:6206(__setattr__)
       24    0.000    0.000    0.001    0.000 generic.py:6553(copy)
       30    0.000    0.000    0.000    0.000 generic.py:659(ndim)
       87    0.000    0.000    0.000    0.000 generic.py:760(_set_axis)
       24    0.000    0.000    0.002    0.000 generic.py:8402(isna)
       15    0.000    0.000    0.001    0.000 indexing.py:1139(__getitem__)
       15    0.000    0.000    0.000    0.000 indexing.py:1188(_validate_key)
       15    0.000    0.000    0.001    0.000 indexing.py:1341(_get_label)
       15    0.000    0.000    0.001    0.000 indexing.py:1359(_getitem_axis)
       37    0.000    0.000    0.000    0.000 indexing.py:2678(check_dict_or_set_indexers)
       15    0.000    0.000    0.000    0.000 indexing.py:289(loc)
       48    0.000    0.000    0.000    0.000 inference.py:105(is_file_like)
       72    0.000    0.000    0.000    0.000 inference.py:273(is_dict_like)
      216    0.000    0.000    0.000    0.000 inference.py:300(<genexpr>)
      301    0.000    0.000    0.000    0.000 inference.py:334(is_hashable)
        1    0.000    0.000    0.040    0.040 main.py:4(main)
       15    0.000    0.000    0.002    0.000 managers.py:1393(idelete)
       37    0.000    0.000    0.000    0.000 managers.py:169(blknos)
       24    0.000    0.000    0.000    0.000 managers.py:1726(is_consolidated)
       24    0.000    0.000    0.000    0.000 managers.py:1734(_consolidate_check)
       24    0.000    0.000    0.000    0.000 managers.py:1740(<listcomp>)
       24    0.000    0.000    0.000    0.000 managers.py:1744(_consolidate_inplace)
       24    0.000    0.000    0.000    0.000 managers.py:1790(ndim)
      109    0.000    0.000    0.000    0.000 managers.py:1799(__init__)
       24    0.000    0.000    0.000    0.000 managers.py:1812(from_blocks)
       48    0.000    0.000    0.000    0.000 managers.py:1825(from_array)
       37    0.000    0.000    0.000    0.000 managers.py:185(blklocs)
       85    0.000    0.000    0.000    0.000 managers.py:1902(_block)
       30    0.000    0.000    0.000    0.000 managers.py:1949(dtype)
        2    0.000    0.000    0.000    0.000 managers.py:1956(external_values)
      155    0.000    0.000    0.000    0.000 managers.py:1960(internal_values)
       24    0.000    0.000    0.001    0.000 managers.py:2068(create_block_manager_from_column_arrays)
      120    0.000    0.000    0.000    0.000 managers.py:2124(_grouping_func)
       24    0.000    0.000    0.001    0.000 managers.py:2137(_form_blocks)
       48    0.000    0.000    0.000    0.000 managers.py:2194(_stack_arrays)
       87    0.000    0.000    0.000    0.000 managers.py:225(set_axis)
       15    0.000    0.000    0.000    0.000 managers.py:2268(_preprocess_slice_or_indexer)
       15    0.000    0.000    0.000    0.000 managers.py:230(is_single_block)
       69    0.000    0.000    0.000    0.000 managers.py:235(items)
       24    0.000    0.000    0.000    0.000 managers.py:308(apply)
       24    0.000    0.000    0.000    0.000 managers.py:335(<dictcomp>)
       15    0.000    0.000    0.000    0.000 managers.py:445(is_view)
       24    0.000    0.000    0.000    0.000 managers.py:540(copy)
       15    0.000    0.000    0.001    0.000 managers.py:691(_slice_take_blocks_ax0)
       39    0.000    0.000    0.000    0.000 managers.py:896(__init__)
       15    0.000    0.000    0.000    0.000 managers.py:941(fast_xs)
       22    0.000    0.000    0.000    0.000 managers.py:991(iget)
       24    0.000    0.000    0.002    0.000 missing.py:101(isna)
       24    0.000    0.000    0.002    0.000 missing.py:184(_isna)
       24    0.000    0.000    0.000    0.000 missing.py:261(_isna_array)
       24    0.000    0.000    0.000    0.000 missing.py:305(_isna_string_dtype)
       24    0.000    0.000    0.000    0.000 missing.py:466(array_equivalent)
       24    0.000    0.000    0.000    0.000 missing.py:564(_array_equivalent_object)
       24    0.000    0.000    0.000    0.000 missing.py:971(clean_reindex_fill_method)
      183    0.000    0.000    0.000    0.000 multiarray.py:1079(copyto)
      120    0.000    0.000    0.000    0.000 multiarray.py:152(concatenate)
       20    0.000    0.000    0.001    0.000 nanops.py:111(f)
       20    0.000    0.000    0.000    0.000 nanops.py:1450(_get_counts)
       20    0.000    0.000    0.000    0.000 nanops.py:1670(_ensure_numeric)
       20    0.000    0.000    0.000    0.000 nanops.py:209(_maybe_get_mask)
       20    0.000    0.000    0.000    0.000 nanops.py:253(_get_values)
       20    0.000    0.000    0.000    0.000 nanops.py:324(_get_dtype_max)
       20    0.000    0.000    0.001    0.000 nanops.py:389(new_func)
       24    0.000    0.000    0.000    0.000 nanops.py:482(nanany)
       20    0.000    0.000    0.001    0.000 nanops.py:671(nanmean)
      183    0.000    0.000    0.001    0.000 numeric.py:290(full)
        4    0.000    0.000    0.000    0.000 numerictypes.py:282(issubclass_)
        2    0.000    0.000    0.000    0.000 numerictypes.py:356(issubdtype)
       25    0.000    0.000    0.000    0.000 parse.py:110(_coerce_args)
       24    0.000    0.000    0.000    0.000 parse.py:365(urlparse)
        1    0.000    0.000    0.000    0.000 parse.py:412(_checknetloc)
        1    0.000    0.000    0.000    0.000 parse.py:432(urlsplit)
       25    0.000    0.000    0.000    0.000 parse.py:99(_noop)
       24    0.000    0.000    0.000    0.000 range.py:134(__new__)
       24    0.000    0.000    0.000    0.000 range.py:198(_simple_new)
       24    0.000    0.000    0.000    0.000 range.py:213(_validate_dtype)
      217    0.000    0.000    0.000    0.000 range.py:963(__len__)
       24    0.000    0.000    0.008    0.000 readers.py:1403(__init__)
       24    0.000    0.000    0.001    0.000 readers.py:1450(close)
       24    0.000    0.000    0.000    0.000 readers.py:1455(_get_options_with_defaults)
       24    0.000    0.000    0.000    0.000 readers.py:1502(_check_file_or_buffer)
       24    0.000    0.000    0.000    0.000 readers.py:1513(_clean_options)
       24    0.000    0.000    0.007    0.000 readers.py:1673(_make_engine)
       24    0.000    0.000    0.018    0.001 readers.py:1732(read)
       24    0.000    0.000    0.000    0.000 readers.py:1779(__enter__)
       24    0.000    0.000    0.001    0.000 readers.py:1782(__exit__)
       24    0.000    0.000    0.000    0.000 readers.py:1850(_clean_na_values)
       24    0.000    0.000    0.000    0.000 readers.py:1925(_refine_defaults_read)
       24    0.000    0.000    0.000    0.000 readers.py:2055(_extract_dialect)
       24    0.000    0.000    0.000    0.000 readers.py:2153(_validate_skipfooter)
       48    0.000    0.000    0.000    0.000 readers.py:518(validate_integer)
       24    0.000    0.000    0.000    0.000 readers.py:550(_validate_names)
       24    0.000    0.000    0.027    0.001 readers.py:574(_read)
       24    0.000    0.000    0.028    0.001 readers.py:848(read_csv)
       22    0.000    0.000    0.000    0.000 series.py:1372(_set_as_cached)
       96    0.000    0.000    0.000    0.000 series.py:1381(_clear_item_cache)
    72/48    0.001    0.000    0.008    0.000 series.py:371(__init__)
       24    0.000    0.000    0.002    0.000 series.py:4960(reindex)
       24    0.000    0.000    0.004    0.000 series.py:524(_init_dict)
       24    0.000    0.000    0.002    0.000 series.py:5478(isna)
       24    0.000    0.000    0.000    0.000 series.py:577(_constructor)
       24    0.000    0.000    0.000    0.000 series.py:581(_constructor_from_mgr)
       44    0.000    0.000    0.001    0.000 series.py:6090(_reduce)
       24    0.000    0.000    0.000    0.000 series.py:6131(any)
       20    0.000    0.000    0.001    0.000 series.py:6213(mean)
       30    0.000    0.000    0.000    0.000 series.py:626(dtype)
       96    0.000    0.000    0.000    0.000 series.py:653(name)
       72    0.000    0.000    0.000    0.000 series.py:703(name)
        2    0.000    0.000    0.000    0.000 series.py:708(values)
      155    0.000    0.000    0.000    0.000 series.py:750(_values)
       15    0.000    0.000    0.000    0.000 series.py:784(_references)
       39    0.000    0.000    0.000    0.000 series.py:821(__len__)
       15    0.000    0.000    0.000    0.000 series.py:905(__array__)
        1    0.000    0.000    0.000    0.000 six.py:194(find_spec)
       30    0.000    0.000    0.000    0.000 take.py:121(_take_nd_ndarray)
        1    0.000    0.000    0.000    0.000 take.py:288(_get_take_nd_function_cached)
       30    0.000    0.000    0.000    0.000 take.py:326(_get_take_nd_function)
       30    0.000    0.000    0.000    0.000 take.py:565(_take_preprocess_indexer_and_fill_value)
       30    0.000    0.000    0.000    0.000 take.py:59(take_nd)
      604    0.000    0.000    0.000    0.000 typing.py:2214(cast)
       15    0.000    0.000    0.000    0.000 utils.py:239(maybe_convert_indices)
       15    0.000    0.000    0.000    0.000 utils.py:62(is_list_like_indexer)
       24    0.000    0.000    0.000    0.000 warnings.py:165(simplefilter)
       24    0.000    0.000    0.000    0.000 warnings.py:181(_add_filter)
       39    0.000    0.000    0.000    0.000 warnings.py:440(__init__)
       39    0.000    0.000    0.000    0.000 warnings.py:466(__enter__)
       39    0.000    0.000    0.000    0.000 warnings.py:487(__exit__)
      214    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF9F3999F90}
      357    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
    50/11    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       24    0.000    0.000    0.000    0.000 {built-in method _codecs.lookup_error}
       24    0.000    0.000    0.000    0.000 {built-in method _codecs.lookup}
       72    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        7    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.find_frozen}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        7    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
      102    0.000    0.000    0.000    0.000 {built-in method _warnings._filters_mutated}
  288/264    0.000    0.000    0.001    0.000 {built-in method builtins.all}
       85    0.000    0.000    0.000    0.000 {built-in method builtins.callable}
        1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
     1935    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      504    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
      358    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.id}
9046/8992    0.001    0.000    0.002    0.000 {built-in method builtins.isinstance}
      523    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
       24    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
3399/2695    0.000    0.000    0.001    0.000 {built-in method builtins.len}
       27    0.000    0.000    0.000    0.000 {built-in method builtins.locals}
       17    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       24    0.000    0.000    0.000    0.000 {built-in method builtins.next}
       24    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
       12    0.004    0.000    0.004    0.000 {built-in method builtins.print}
       20    0.000    0.000    0.000    0.000 {built-in method builtins.round}
       48    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
       24    0.002    0.000    0.002    0.000 {built-in method io.open}
       72    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        9    0.000    0.000    0.000    0.000 {built-in method nt.stat}
       48    0.000    0.000    0.000    0.000 {built-in method numpy.array}
  308/293    0.000    0.000    0.000    0.000 {built-in method numpy.asarray}
      323    0.000    0.000    0.001    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
      357    0.000    0.000    0.000    0.000 {built-in method numpy.empty}
       15    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       24    0.000    0.000    0.000    0.000 {built-in method pandas._libs.missing.isnaobj}
       24    0.000    0.000    0.000    0.000 {built-in method sys.getfilesystemencoding}
        2    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
       22    0.000    0.000    0.000    0.000 {method '_rebuild_blknos_and_blklocs' of 'pandas._libs.internals.BlockManager' objects}
        2    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
      104    0.000    0.000    0.000    0.000 {method 'add_index_reference' of 'pandas._libs.internals.BlockValuesRefs' objects}
       54    0.000    0.000    0.000    0.000 {method 'any' of 'numpy.ndarray' objects}
      446    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       15    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       15    0.000    0.000    0.000    0.000 {method 'clear_mapping' of 'pandas._libs.index.IndexEngine' objects}
       24    0.001    0.000    0.001    0.000 {method 'close' of '_io.TextIOWrapper' objects}
       24    0.000    0.000    0.000    0.000 {method 'close' of 'pandas._libs.parsers.TextReader' objects}
       74    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
       24    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
      351    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       22    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
     1792    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       52    0.000    0.000    0.000    0.000 {method 'get_loc' of 'pandas._libs.index.IndexEngine' objects}
       24    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'isalpha' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'isascii' of 'str' objects}
      142    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       69    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       48    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
      217    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       24    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       15    0.000    0.000    0.000    0.000 {method 'max' of 'numpy.ndarray' objects}
       15    0.000    0.000    0.000    0.000 {method 'nonzero' of 'numpy.ndarray' objects}
      456    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
      120    0.000    0.000    0.000    0.000 {method 'pop' of 'set' objects}
       24    0.001    0.000    0.001    0.000 {method 'read_low_memory' of 'pandas._libs.parsers.TextReader' objects}
      109    0.001    0.000    0.001    0.000 {method 'reduce' of 'numpy.ufunc' objects}
       24    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
        6    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       24    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
       10    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
      138    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       72    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       18    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}
      163    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       20    0.000    0.000    0.000    0.000 {method 'sum' of 'numpy.ndarray' objects}
       26    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       48    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
       48    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       48    0.000    0.000    0.000    0.000 {pandas._libs.algos.ensure_object}
       45    0.000    0.000    0.000    0.000 {pandas._libs.algos.ensure_platform_int}
       30    0.000    0.000    0.000    0.000 {pandas._libs.algos.take_1d_int64_int64}
       15    0.000    0.000    0.000    0.000 {pandas._libs.internals.get_blkno_placements}
       24    0.000    0.000    0.000    0.000 {pandas._libs.lib.array_equivalent_object}
      120    0.000    0.000    0.000    0.000 {pandas._libs.lib.dtypes_all_equal}
       48    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_all_arraylike}
       83    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_bool}
       96    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_float}
      172    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_integer}
      133    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_iterator}
      486    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_list_like}
      252    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_np_dtype}
      126    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_scalar}
       37    0.000    0.000    0.000    0.000 {pandas._libs.lib.item_from_zerodim}
      183    0.001    0.000    0.001    0.000 {pandas._libs.lib.maybe_convert_objects}
       15    0.000    0.000    0.000    0.000 {pandas._libs.lib.maybe_indices_to_slice}
```

## Unittests

```bash
17020 function calls (16756 primitive calls) in 0.021 seconds

   Ordered by: standard name
   
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       50    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(copyto)
        7    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(prod)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:113(__subclasshook__)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:156(__subclasshook__)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:262(__subclasshook__)
        5    0.000    0.000    0.000    0.000 <frozen _collections_abc>:283(__subclasshook__)
        6    0.000    0.000    0.000    0.000 <frozen _collections_abc>:315(__subclasshook__)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:362(__subclasshook__)
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:381(__subclasshook__)
        6    0.000    0.000    0.000    0.000 <frozen _collections_abc>:78(_check_methods)
      104    0.000    0.000    0.000    0.000 <frozen abc>:117(__instancecheck__)
     20/7    0.000    0.000    0.000    0.000 <frozen abc>:121(__subclasscheck__)
        5    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
        5    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
       82    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1103(_sanity_check)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1167(_find_and_load)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1194(_gcd_import)
       11    0.000    0.000    0.000    0.000 <string>:1(<lambda>)
        1    0.000    0.000    0.021    0.021 <string>:1(<module>)
       12    0.000    0.000    0.000    0.000 __init__.py:108(import_module)
        1    0.000    0.000    0.001    0.001 __init__.py:225(compile)
        1    0.000    0.000    0.001    0.001 __init__.py:272(_compile)
       23    0.000    0.000    0.000    0.000 __init__.py:33(using_copy_on_write)
       14    0.000    0.000    0.000    0.000 __init__.py:43(using_pyarrow_string_dtype)
        4    0.000    0.000    0.000    0.000 __init__.py:440(_make)
       12    0.000    0.000    0.000    0.000 _asarray.py:112(<setcomp>)
       12    0.000    0.000    0.000    0.000 _asarray.py:31(require)
        8    0.000    0.000    0.000    0.000 _compiler.py:214(_compile_charset)
        8    0.000    0.000    0.000    0.000 _compiler.py:241(_optimize_charset)
        9    0.000    0.000    0.000    0.000 _compiler.py:31(_combine_flags)
     22/1    0.000    0.000    0.000    0.000 _compiler.py:37(_compile)
        8    0.000    0.000    0.000    0.000 _compiler.py:396(_simple)
        2    0.000    0.000    0.000    0.000 _compiler.py:426(_get_iscased)
        1    0.000    0.000    0.000    0.000 _compiler.py:434(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 _compiler.py:465(_get_charset_prefix)
        1    0.000    0.000    0.000    0.000 _compiler.py:509(_compile_info)
        2    0.000    0.000    0.000    0.000 _compiler.py:568(isstring)
        1    0.000    0.000    0.000    0.000 _compiler.py:571(_code)
        1    0.000    0.000    0.001    0.001 _compiler.py:738(compile)
        2    0.000    0.000    0.000    0.000 _dtype.py:24(_kind_name)
        2    0.000    0.000    0.000    0.000 _dtype.py:330(_name_includes_bit_suffix)
        2    0.000    0.000    0.000    0.000 _dtype.py:344(_name_get)
        2    0.000    0.000    0.000    0.000 _methods.py:39(_amax)
        7    0.000    0.000    0.000    0.000 _methods.py:47(_sum)
        4    0.000    0.000    0.000    0.000 _methods.py:55(_any)
       22    0.000    0.000    0.000    0.000 _parser.py:109(__init__)
       38    0.000    0.000    0.000    0.000 _parser.py:158(__len__)
      121    0.000    0.000    0.000    0.000 _parser.py:162(__getitem__)
        8    0.000    0.000    0.000    0.000 _parser.py:166(__setitem__)
       26    0.000    0.000    0.000    0.000 _parser.py:170(append)
    27/10    0.000    0.000    0.000    0.000 _parser.py:172(getwidth)
        1    0.000    0.000    0.000    0.000 _parser.py:222(__init__)
       77    0.000    0.000    0.000    0.000 _parser.py:231(__next)
       59    0.000    0.000    0.000    0.000 _parser.py:247(match)
       41    0.000    0.000    0.000    0.000 _parser.py:252(get)
        3    0.000    0.000    0.000    0.000 _parser.py:265(getuntil)
       35    0.000    0.000    0.000    0.000 _parser.py:284(tell)
        3    0.000    0.000    0.000    0.000 _parser.py:295(checkgroupname)
       10    0.000    0.000    0.000    0.000 _parser.py:367(_escape)
     14/1    0.000    0.000    0.000    0.000 _parser.py:447(_parse_sub)
     14/1    0.000    0.000    0.000    0.000 _parser.py:507(_parse)
        1    0.000    0.000    0.000    0.000 _parser.py:73(__init__)
       20    0.000    0.000    0.000    0.000 _parser.py:79(groups)
        9    0.000    0.000    0.000    0.000 _parser.py:82(opengroup)
        9    0.000    0.000    0.000    0.000 _parser.py:94(closegroup)
        1    0.000    0.000    0.000    0.000 _parser.py:954(fix_flags)
        1    0.000    0.000    0.000    0.000 _parser.py:970(parse)
       11    0.000    0.000    0.000    0.000 _validators.py:226(validate_bool_kwarg)
        6    0.000    0.000    0.000    0.000 api.py:379(default_index)
       19    0.000    0.000    0.000    0.000 ast.py:33(parse)
        5    0.000    0.000    0.000    0.000 base.py:2292(is_unique)
       12    0.000    0.000    0.000    0.000 base.py:3762(get_loc)
        9    0.000    0.000    0.000    0.000 base.py:458(_engine_type)
        8    0.000    0.000    0.001    0.000 base.py:477(__new__)
        2    0.000    0.000    0.000    0.000 base.py:5070(values)
       27    0.000    0.000    0.000    0.000 base.py:5126(_values)
        9    0.000    0.000    0.000    0.000 base.py:5152(_get_engine_target)
       21    0.000    0.000    0.000    0.000 base.py:5299(__contains__)
       22    0.000    0.000    0.000    0.000 base.py:5349(__getitem__)
       12    0.000    0.000    0.000    0.000 base.py:538(<genexpr>)
        2    0.000    0.000    0.000    0.000 base.py:5391(_getitem_slice)
        8    0.000    0.000    0.000    0.000 base.py:573(_ensure_array)
        8    0.000    0.000    0.000    0.000 base.py:591(_dtype_to_subclass)
        2    0.000    0.000    0.000    0.000 base.py:61(__len__)
       12    0.000    0.000    0.000    0.000 base.py:648(_simple_new)
       12    0.000    0.000    0.000    0.000 base.py:6611(_maybe_cast_indexer)
        9    0.000    0.000    0.000    0.000 base.py:69(shape)
        2    0.000    0.000    0.000    0.000 base.py:691(_constructor)
       27    0.000    0.000    0.000    0.000 base.py:71(<genexpr>)
        2    0.000    0.000    0.000    0.000 base.py:73(_validate_set_axis)
        2    0.000    0.000    0.000    0.000 base.py:7472(ensure_index_from_sequences)
       14    0.000    0.000    0.000    0.000 base.py:7512(ensure_index)
        8    0.000    0.000    0.000    0.000 base.py:7607(maybe_extract_name)
       18    0.000    0.000    0.000    0.000 base.py:830(_reset_identity)
        2    0.000    0.000    0.000    0.000 base.py:837(_cleanup)
        9    0.000    0.000    0.000    0.000 base.py:841(_engine)
       19    0.000    0.000    0.000    0.000 base.py:908(__len__)
        9    0.000    0.000    0.000    0.000 base.py:973(dtype)
       10    0.000    0.000    0.000    0.000 blocks.py:1007(iget)
        2    0.000    0.000    0.000    0.000 blocks.py:1016(_slice)
       12    0.000    0.000    0.000    0.000 blocks.py:187(is_extension)
       12    0.000    0.000    0.000    0.000 blocks.py:192(_can_consolidate)
        2    0.000    0.000    0.000    0.000 blocks.py:222(external_values)
        2    0.000    0.000    0.000    0.000 blocks.py:2236(is_view)
       14    0.000    0.000    0.000    0.000 blocks.py:2346(get_block_type)
        2    0.000    0.000    0.000    0.000 blocks.py:2388(new_block)
        2    0.000    0.000    0.000    0.000 blocks.py:2586(external_values)
        2    0.000    0.000    0.000    0.000 blocks.py:323(getitem_block_columns)
       14    0.000    0.000    0.000    0.000 blocks.py:583(dtype)
        1    0.000    0.000    0.000    0.000 case.py:1063(_truncateMessage)
        1    0.000    0.000    0.001    0.001 case.py:1162(assertDictEqual)
        1    0.000    0.000    0.000    0.000 case.py:1235(assertMultiLineEqual)
        4    0.000    0.000    0.000    0.000 case.py:1291(assertIsInstance)
        1    0.000    0.000    0.000    0.000 case.py:131(doModuleCleanups)
        6    0.000    0.000    0.000    0.000 case.py:393(__init__)
       36    0.000    0.000    0.000    0.000 case.py:425(addTypeEqualityFunc)
        6    0.000    0.000    0.000    0.000 case.py:45(__init__)
        6    0.000    0.000    0.000    0.000 case.py:471(tearDown)
        1    0.000    0.000    0.000    0.000 case.py:475(setUpClass)
        1    0.000    0.000    0.000    0.000 case.py:479(tearDownClass)
        6    0.000    0.000    0.000    0.000 case.py:483(countTestCases)
        5    0.000    0.000    0.000    0.000 case.py:489(shortDescription)
        5    0.000    0.000    0.000    0.000 case.py:512(__str__)
       36    0.000    0.000    0.005    0.000 case.py:52(testPartExecutor)
        6    0.000    0.000    0.002    0.000 case.py:575(_callSetUp)
        6    0.000    0.000    0.006    0.001 case.py:578(_callTestMethod)
        6    0.000    0.000    0.000    0.000 case.py:583(_callTearDown)
        6    0.000    0.000    0.013    0.002 case.py:589(run)
        6    0.000    0.000    0.000    0.000 case.py:652(doCleanups)
        1    0.000    0.000    0.000    0.000 case.py:665(doClassCleanups)
        6    0.000    0.000    0.013    0.002 case.py:677(__call__)
        1    0.000    0.000    0.000    0.000 case.py:701(fail)
        1    0.000    0.000    0.000    0.000 case.py:717(_formatMessage)
        6    0.000    0.000    0.000    0.000 case.py:835(_getAssertEqualityFunc)
        4    0.000    0.000    0.000    0.000 case.py:861(_baseAssertEqual)
        6    0.000    0.000    0.001    0.000 case.py:868(assertEqual)
        5    0.000    0.000    0.005    0.001 case.py:94(_addError)
       14    0.000    0.000    0.000    0.000 cast.py:1147(maybe_infer_to_datetimelike)
       36    0.000    0.000    0.000    0.000 cast.py:119(maybe_convert_platform)
       36    0.000    0.000    0.000    0.000 cast.py:1544(construct_1d_object_array_from_listlike)
        9    0.000    0.000    0.000    0.000 common.py:1025(needs_i8_conversion)
        2    0.000    0.000    0.000    0.000 common.py:1183(is_bool_dtype)
       30    0.000    0.000    0.000    0.000 common.py:1255(is_1d_only_ea_dtype)
       16    0.000    0.000    0.000    0.000 common.py:1322(is_ea_or_datetimelike_dtype)
        2    0.000    0.000    0.000    0.000 common.py:1390(_get_dtype)
       18    0.000    0.000    0.000    0.000 common.py:149(cast_scalar_indexer)
        2    0.000    0.000    0.000    0.000 common.py:228(asarray_tuplesafe)
       30    0.000    0.000    0.000    0.000 common.py:296(maybe_iterable_to_list)
       11    0.000    0.000    0.000    0.000 common.py:367(apply_if_callable)
       30    0.000    0.000    0.000    0.000 common.py:556(require_length_match)
        4    0.000    0.000    0.000    0.000 common.py:96(is_bool_indexer)
        6    0.000    0.000    0.000    0.000 config.py:127(_get_single_key)
        6    0.000    0.000    0.000    0.000 config.py:145(_get_option)
        6    0.000    0.000    0.000    0.000 config.py:271(__call__)
        6    0.000    0.000    0.000    0.000 config.py:615(_select_options)
        6    0.000    0.000    0.000    0.000 config.py:633(_get_root)
       12    0.000    0.000    0.000    0.000 config.py:647(_get_deprecated_option)
        6    0.000    0.000    0.000    0.000 config.py:674(_translate_key)
        6    0.000    0.000    0.000    0.000 config.py:686(_warn_if_deprecated)
        6    0.000    0.000    0.000    0.000 construction.py:196(mgr_to_mgr)
       38    0.000    0.000    0.000    0.000 construction.py:419(extract_array)
        6    0.000    0.000    0.002    0.000 construction.py:423(dict_to_mgr)
        6    0.000    0.000    0.000    0.000 construction.py:481(<listcomp>)
        8    0.000    0.000    0.000    0.000 construction.py:484(ensure_wrapped_if_datetimelike)
        6    0.000    0.000    0.000    0.000 construction.py:487(<listcomp>)
       38    0.000    0.000    0.001    0.000 construction.py:518(sanitize_array)
        6    0.000    0.000    0.001    0.000 construction.py:596(_homogenize)
        6    0.000    0.000    0.000    0.000 construction.py:638(_extract_index)
       36    0.000    0.000    0.000    0.000 construction.py:665(_sanitize_non_ordered)
       38    0.000    0.000    0.000    0.000 construction.py:673(_sanitize_ndim)
       38    0.000    0.000    0.000    0.000 construction.py:712(_sanitize_str_dtypes)
       38    0.000    0.000    0.000    0.000 construction.py:732(_maybe_repeat)
        6    0.000    0.000    0.001    0.000 construction.py:96(arrays_to_mgr)
       24    0.000    0.000    0.000    0.000 contextlib.py:104(__init__)
       24    0.000    0.000    0.003    0.000 contextlib.py:132(__enter__)
       24    0.000    0.000    0.005    0.000 contextlib.py:141(__exit__)
       24    0.000    0.000    0.000    0.000 contextlib.py:287(helper)
       19    0.000    0.000    0.000    0.000 contextlib.py:428(__init__)
       19    0.000    0.000    0.000    0.000 contextlib.py:431(__enter__)
       19    0.000    0.000    0.000    0.000 contextlib.py:434(__exit__)
        6    0.000    0.000    0.000    0.000 contextlib.py:450(_create_exit_wrapper)
       12    0.000    0.000    0.000    0.000 contextlib.py:460(__init__)
        6    0.000    0.000    0.003    0.000 contextlib.py:490(enter_context)
        6    0.000    0.000    0.000    0.000 contextlib.py:522(_push_cm_exit)
        6    0.000    0.000    0.000    0.000 contextlib.py:527(_push_exit_callback)
        6    0.000    0.000    0.000    0.000 contextlib.py:543(__enter__)
     12/6    0.000    0.000    0.000    0.000 contextlib.py:546(__exit__)
      156    0.000    0.000    0.001    0.000 coroutines.py:21(iscoroutinefunction)
       20    0.000    0.000    0.000    0.000 difflib.py:1061(IS_CHARACTER_JUNK)
        2    0.000    0.000    0.000    0.000 difflib.py:120(__init__)
        1    0.000    0.000    0.000    0.000 difflib.py:1303(ndiff)
        3    0.000    0.000    0.000    0.000 difflib.py:184(set_seqs)
        4    0.000    0.000    0.000    0.000 difflib.py:196(set_seq1)
        4    0.000    0.000    0.000    0.000 difflib.py:222(set_seq2)
        3    0.000    0.000    0.000    0.000 difflib.py:266(__chain_b)
       11    0.000    0.000    0.000    0.000 difflib.py:305(find_longest_match)
        4    0.000    0.000    0.000    0.000 difflib.py:39(_calculate_ratio)
        4    0.000    0.000    0.000    0.000 difflib.py:421(get_matching_blocks)
        2    0.000    0.000    0.000    0.000 difflib.py:492(get_opcodes)
        2    0.000    0.000    0.000    0.000 difflib.py:597(ratio)
        8    0.000    0.000    0.000    0.000 difflib.py:619(<genexpr>)
        1    0.000    0.000    0.000    0.000 difflib.py:622(quick_ratio)
        1    0.000    0.000    0.000    0.000 difflib.py:651(real_quick_ratio)
        2    0.000    0.000    0.000    0.000 difflib.py:715(_keep_original_ws)
      138    0.000    0.000    0.000    0.000 difflib.py:717(<genexpr>)
        1    0.000    0.000    0.000    0.000 difflib.py:810(__init__)
        5    0.000    0.000    0.000    0.000 difflib.py:833(compare)
        5    0.000    0.000    0.000    0.000 difflib.py:893(_fancy_replace)
        2    0.000    0.000    0.000    0.000 difflib.py:987(_fancy_helper)
        5    0.000    0.000    0.000    0.000 difflib.py:999(_qformat)
        2    0.000    0.000    0.000    0.000 enum.py:1096(__new__)
        1    0.000    0.000    0.000    0.000 enum.py:1248(value)
        2    0.000    0.000    0.000    0.000 enum.py:1504(__and__)
        1    0.000    0.000    0.000    0.000 enum.py:192(__get__)
        2    0.000    0.000    0.000    0.000 enum.py:691(__call__)
       16    0.000    0.000    0.000    0.000 flags.py:53(__init__)
       14    0.000    0.000    0.000    0.000 flags.py:57(allows_duplicate_labels)
       10    0.000    0.000    0.000    0.000 flags.py:89(allows_duplicate_labels)
        2    0.000    0.000    0.000    0.000 frame.py:1542(__len__)
        8    0.000    0.000    0.000    0.000 frame.py:3779(_ixs)
        9    0.000    0.000    0.001    0.000 frame.py:3856(__getitem__)
        8    0.000    0.000    0.000    0.000 frame.py:4387(_box_col_values)
        2    0.000    0.000    0.000    0.000 frame.py:4402(_clear_item_cache)
        9    0.000    0.000    0.000    0.000 frame.py:4405(_get_item_cache)
        4    0.000    0.000    0.001    0.000 frame.py:5744(set_index)
       10    0.000    0.000    0.000    0.000 frame.py:653(_sliced_from_mgr)
       10    0.000    0.000    0.000    0.000 frame.py:656(_constructor_sliced_from_mgr)
        6    0.000    0.000    0.002    0.000 frame.py:668(__init__)
        2    0.000    0.000    0.000    0.000 frame.py:952(axes)
        7    0.000    0.000    0.000    0.000 fromnumeric.py:2950(_prod_dispatcher)
        7    0.000    0.000    0.000    0.000 fromnumeric.py:2955(prod)
        7    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
        7    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
        7    0.000    0.000    0.000    0.000 function.py:411(validate_func)
        7    0.000    0.000    0.000    0.000 function.py:64(__call__)
        2    0.000    0.000    0.000    0.000 functions.py:11(get_all_student_names)
        6    0.000    0.000    0.001    0.000 functions.py:18(calculate_average_mark_for_test)
        4    0.000    0.000    0.001    0.000 functions.py:29(calculate_average_mark_for_student)
        1    0.000    0.000    0.000    0.000 functions.py:44(get_all_tests_average_marks)
        1    0.000    0.000    0.001    0.001 functions.py:52(get_all_failed_students)
        2    0.000    0.000    0.000    0.000 functions.py:6(get_all_test_names)
      156    0.000    0.000    0.000    0.000 functools.py:421(_unwrap_partial)
        7    0.000    0.000    0.000    0.000 generic.py:11920(_stat_function)
        7    0.000    0.000    0.000    0.000 generic.py:11971(mean)
       16    0.000    0.000    0.000    0.000 generic.py:274(__init__)
       10    0.000    0.000    0.000    0.000 generic.py:335(_from_mgr)
       10    0.000    0.000    0.000    0.000 generic.py:358(attrs)
      164    0.000    0.000    0.000    0.000 generic.py:37(_check)
       24    0.000    0.000    0.000    0.000 generic.py:393(flags)
        2    0.000    0.000    0.000    0.000 generic.py:4094(xs)
      164    0.000    0.000    0.000    0.000 generic.py:42(_instancecheck)
        2    0.000    0.000    0.000    0.000 generic.py:4314(_set_is_copy)
        2    0.000    0.000    0.000    0.000 generic.py:4412(__delitem__)
        4    0.000    0.000    0.000    0.000 generic.py:4453(_check_inplace_and_allows_duplicate_labels)
        2    0.000    0.000    0.000    0.000 generic.py:4520(_is_view)
       15    0.000    0.000    0.000    0.000 generic.py:548(_get_axis_number)
        6    0.000    0.000    0.000    0.000 generic.py:562(_get_axis)
       10    0.000    0.000    0.000    0.000 generic.py:6147(__finalize__)
        4    0.000    0.000    0.000    0.000 generic.py:6189(__getattr__)
       42    0.000    0.000    0.000    0.000 generic.py:6206(__setattr__)
        4    0.000    0.000    0.000    0.000 generic.py:659(ndim)
        2    0.000    0.000    0.000    0.000 generic.py:760(_set_axis)
        2    0.000    0.000    0.000    0.000 indexing.py:1139(__getitem__)
        2    0.000    0.000    0.000    0.000 indexing.py:1188(_validate_key)
        2    0.000    0.000    0.000    0.000 indexing.py:1341(_get_label)
        2    0.000    0.000    0.000    0.000 indexing.py:1359(_getitem_axis)
       11    0.000    0.000    0.000    0.000 indexing.py:2678(check_dict_or_set_indexers)
        2    0.000    0.000    0.000    0.000 indexing.py:289(loc)
       17    0.000    0.000    0.000    0.000 inference.py:334(is_hashable)
      150    0.000    0.000    0.000    0.000 inspect.py:2075(_signature_is_functionlike)
       84    0.000    0.000    0.000    0.000 inspect.py:2736(name)
        6    0.000    0.000    0.000    0.000 inspect.py:2740(default)
      168    0.000    0.000    0.000    0.000 inspect.py:2748(kind)
        6    0.000    0.000    0.000    0.000 inspect.py:2828(__init__)
      144    0.000    0.000    0.000    0.000 inspect.py:292(isclass)
      156    0.000    0.000    0.000    0.000 inspect.py:300(ismethod)
        6    0.000    0.000    0.000    0.000 inspect.py:3031(parameters)
        6    0.000    0.000    0.000    0.000 inspect.py:3075(_bind)
        6    0.000    0.000    0.000    0.000 inspect.py:3213(bind_partial)
      156    0.000    0.000    0.000    0.000 inspect.py:378(isfunction)
      156    0.000    0.000    0.001    0.000 inspect.py:391(_has_code_flag)
      156    0.000    0.000    0.001    0.000 inspect.py:409(iscoroutinefunction)
        6    0.000    0.000    0.000    0.000 inspect.py:449(isawaitable)
       19    0.000    0.000    0.000    0.000 linecache.py:147(lazycache)
       19    0.000    0.000    0.002    0.000 linecache.py:26(getline)
       19    0.000    0.000    0.002    0.000 linecache.py:36(getlines)
       16    0.000    0.000    0.001    0.000 linecache.py:52(checkcache)
        5    0.000    0.000    0.002    0.000 linecache.py:80(updatecache)
        1    0.000    0.000    0.000    0.000 loader.py:223(getTestCaseNames)
      120    0.000    0.000    0.000    0.000 loader.py:226(shouldIncludeMethod)
        1    0.000    0.000    0.000    0.000 loader.py:77(__init__)
        1    0.000    0.000    0.000    0.000 loader.py:84(loadTestsFromTestCase)
        2    0.000    0.000    0.000    0.000 managers.py:1393(idelete)
       10    0.000    0.000    0.000    0.000 managers.py:169(blknos)
        6    0.000    0.000    0.000    0.000 managers.py:1726(is_consolidated)
        6    0.000    0.000    0.000    0.000 managers.py:1734(_consolidate_check)
        6    0.000    0.000    0.000    0.000 managers.py:1740(<listcomp>)
        6    0.000    0.000    0.000    0.000 managers.py:1744(_consolidate_inplace)
       10    0.000    0.000    0.000    0.000 managers.py:1799(__init__)
       10    0.000    0.000    0.000    0.000 managers.py:185(blklocs)
       10    0.000    0.000    0.000    0.000 managers.py:1902(_block)
        4    0.000    0.000    0.000    0.000 managers.py:1949(dtype)
        2    0.000    0.000    0.000    0.000 managers.py:1956(external_values)
        9    0.000    0.000    0.000    0.000 managers.py:1960(internal_values)
        6    0.000    0.000    0.000    0.000 managers.py:2068(create_block_manager_from_column_arrays)
       30    0.000    0.000    0.000    0.000 managers.py:2124(_grouping_func)
        6    0.000    0.000    0.000    0.000 managers.py:2137(_form_blocks)
       12    0.000    0.000    0.000    0.000 managers.py:2194(_stack_arrays)
        2    0.000    0.000    0.000    0.000 managers.py:225(set_axis)
        2    0.000    0.000    0.000    0.000 managers.py:2268(_preprocess_slice_or_indexer)
        2    0.000    0.000    0.000    0.000 managers.py:230(is_single_block)
        6    0.000    0.000    0.000    0.000 managers.py:235(items)
        2    0.000    0.000    0.000    0.000 managers.py:445(is_view)
        2    0.000    0.000    0.000    0.000 managers.py:691(_slice_take_blocks_ax0)
        8    0.000    0.000    0.000    0.000 managers.py:896(__init__)
        2    0.000    0.000    0.000    0.000 managers.py:941(fast_xs)
        8    0.000    0.000    0.000    0.000 managers.py:991(iget)
        6    0.000    0.000    0.000    0.000 mock.py:1079(_try_iter)
        6    0.000    0.000    0.001    0.000 mock.py:1096(__init__)
       14    0.000    0.000    0.000    0.000 mock.py:1108(_mock_check_sig)
       14    0.000    0.000    0.000    0.000 mock.py:1113(__call__)
       14    0.000    0.000    0.000    0.000 mock.py:1121(_mock_call)
       14    0.000    0.000    0.000    0.000 mock.py:1124(_increment_mock_call)
       14    0.000    0.000    0.000    0.000 mock.py:1170(_execute_mock_call)
       12    0.000    0.000    0.003    0.000 mock.py:1343(decoration_helper)
        6    0.000    0.000    0.006    0.001 mock.py:1364(patched)
        6    0.000    0.000    0.000    0.000 mock.py:1392(get_original)
        6    0.000    0.000    0.003    0.000 mock.py:1416(__enter__)
        6    0.000    0.000    0.000    0.000 mock.py:1562(__exit__)
        6    0.000    0.000    0.001    0.000 mock.py:2098(__init__)
       12    0.000    0.000    0.001    0.000 mock.py:2104(_mock_set_magics)
      462    0.000    0.000    0.000    0.000 mock.py:2169(__init__)
       28    0.000    0.000    0.000    0.000 mock.py:2469(__new__)
       28    0.000    0.000    0.000    0.000 mock.py:2501(__init__)
       42    0.000    0.000    0.000    0.000 mock.py:326(_get)
       42    0.000    0.000    0.000    0.000 mock.py:331(_set)
        6    0.000    0.000    0.000    0.000 mock.py:362(_check_and_set_parent)
        6    0.000    0.000    0.000    0.000 mock.py:398(__init__)
        6    0.000    0.000    0.000    0.000 mock.py:414(__new__)
        6    0.000    0.000    0.001    0.000 mock.py:430(__init__)
        6    0.000    0.000    0.001    0.000 mock.py:499(_mock_add_spec)
        6    0.000    0.000    0.000    0.000 mock.py:53(_is_async_obj)
       14    0.000    0.000    0.000    0.000 mock.py:530(__get_return_value)
        6    0.000    0.000    0.000    0.000 mock.py:543(__set_return_value)
       14    0.000    0.000    0.000    0.000 mock.py:568(__get_side_effect)
        6    0.000    0.000    0.000    0.000 mock.py:579(__set_side_effect)
        6    0.000    0.000    0.000    0.000 mock.py:642(__getattr__)
       18    0.000    0.000    0.000    0.000 mock.py:68(_is_instance_mock)
    66/54    0.000    0.000    0.000    0.000 mock.py:756(__setattr__)
        6    0.000    0.000    0.000    0.000 mock.py:81(_extract_mock)
        1    0.000    0.000    0.000    0.000 mocks.py:19(test_get_all_test_names)
        1    0.000    0.000    0.000    0.000 mocks.py:26(test_get_all_student_names)
        1    0.000    0.000    0.000    0.000 mocks.py:34(test_calculate_average_mark_for_test)
        1    0.000    0.000    0.001    0.001 mocks.py:44(test_calculate_average_mark_for_student)
        1    0.000    0.000    0.001    0.001 mocks.py:54(test_get_all_tests_average_marks)
        1    0.000    0.000    0.001    0.001 mocks.py:62(test_get_all_failed_students)
        1    0.000    0.000    0.021    0.021 mocks.py:70(run_tests)
        6    0.000    0.000    0.002    0.000 mocks.py:9(setUp)
       50    0.000    0.000    0.000    0.000 multiarray.py:1079(copyto)
        7    0.000    0.000    0.000    0.000 nanops.py:111(f)
        7    0.000    0.000    0.000    0.000 nanops.py:1450(_get_counts)
        7    0.000    0.000    0.000    0.000 nanops.py:1670(_ensure_numeric)
        7    0.000    0.000    0.000    0.000 nanops.py:209(_maybe_get_mask)
        7    0.000    0.000    0.000    0.000 nanops.py:253(_get_values)
        7    0.000    0.000    0.000    0.000 nanops.py:324(_get_dtype_max)
        7    0.000    0.000    0.000    0.000 nanops.py:389(new_func)
        7    0.000    0.000    0.000    0.000 nanops.py:671(nanmean)
       50    0.000    0.000    0.000    0.000 numeric.py:290(full)
        4    0.000    0.000    0.000    0.000 numerictypes.py:282(issubclass_)
        2    0.000    0.000    0.000    0.000 numerictypes.py:356(issubdtype)
       12    0.000    0.000    0.001    0.000 pkgutil.py:645(resolve_name)
        8    0.000    0.000    0.000    0.000 pprint.py:102(_safe_tuple)
        2    0.000    0.000    0.000    0.000 pprint.py:107(__init__)
        2    0.000    0.000    0.000    0.000 pprint.py:156(pformat)
        2    0.000    0.000    0.000    0.000 pprint.py:168(_format)
        2    0.000    0.000    0.000    0.000 pprint.py:454(_repr)
     18/2    0.000    0.000    0.000    0.000 pprint.py:463(format)
     18/2    0.000    0.000    0.000    0.000 pprint.py:551(_safe_repr)
        2    0.000    0.000    0.000    0.000 pprint.py:57(pformat)
       16    0.000    0.000    0.000    0.000 pprint.py:92(__init__)
        6    0.000    0.000    0.000    0.000 pprint.py:95(__lt__)
        6    0.000    0.000    0.000    0.000 range.py:198(_simple_new)
       45    0.000    0.000    0.000    0.000 range.py:963(__len__)
        1    0.000    0.000    0.000    0.000 result.py:104(stopTestRun)
        4    0.000    0.000    0.004    0.001 result.py:110(addError)
        1    0.000    0.000    0.000    0.000 result.py:118(addFailure)
        5    0.000    0.000    0.004    0.001 result.py:13(inner)
        1    0.000    0.000    0.000    0.000 result.py:142(addSuccess)
        1    0.000    0.000    0.000    0.000 result.py:160(wasSuccessful)
        5    0.000    0.000    0.004    0.001 result.py:173(_exc_info_to_string)
        5    0.000    0.000    0.000    0.000 result.py:195(_clean_tracebacks)
       23    0.000    0.000    0.000    0.000 result.py:223(_is_relevant_tb_level)
        1    0.000    0.000    0.000    0.000 result.py:226(_remove_unittest_tb_frames)
        1    0.000    0.000    0.000    0.000 result.py:38(__init__)
        6    0.000    0.000    0.000    0.000 result.py:58(startTest)
        9    0.000    0.000    0.000    0.000 result.py:64(_setupStdout)
        1    0.000    0.000    0.000    0.000 result.py:72(startTestRun)
        6    0.000    0.000    0.000    0.000 result.py:78(stopTest)
        9    0.000    0.000    0.000    0.000 result.py:83(_restoreStdout)
        1    0.000    0.000    0.001    0.001 runner.py:105(addFailure)
        1    0.000    0.000    0.007    0.007 runner.py:139(printErrors)
        2    0.000    0.000    0.007    0.003 runner.py:152(printErrorList)
        1    0.000    0.000    0.000    0.000 runner.py:16(__init__)
        1    0.000    0.000    0.000    0.000 runner.py:169(__init__)
        1    0.000    0.000    0.000    0.000 runner.py:189(_makeResult)
       68    0.000    0.000    0.000    0.000 runner.py:19(__getattr__)
        1    0.000    0.000    0.021    0.021 runner.py:192(run)
       25    0.000    0.000    0.007    0.000 runner.py:24(writeln)
        1    0.000    0.000    0.000    0.000 runner.py:38(__init__)
        5    0.000    0.000    0.000    0.000 runner.py:46(getDescription)
        6    0.000    0.000    0.000    0.000 runner.py:53(startTest)
        1    0.000    0.000    0.000    0.000 runner.py:89(addSuccess)
        4    0.000    0.000    0.004    0.001 runner.py:97(addError)
        8    0.000    0.000    0.000    0.000 series.py:1372(_set_as_cached)
        7    0.000    0.000    0.000    0.000 series.py:6090(_reduce)
        7    0.000    0.000    0.000    0.000 series.py:6213(mean)
        4    0.000    0.000    0.000    0.000 series.py:626(dtype)
        2    0.000    0.000    0.000    0.000 series.py:708(values)
        9    0.000    0.000    0.000    0.000 series.py:750(_values)
        2    0.000    0.000    0.000    0.000 series.py:784(_references)
        2    0.000    0.000    0.000    0.000 series.py:821(__len__)
        2    0.000    0.000    0.000    0.000 series.py:905(__array__)
        1    0.000    0.000    0.000    0.000 signals.py:42(registerResult)
        1    0.000    0.000    0.013    0.013 suite.py:102(run)
        6    0.000    0.000    0.000    0.000 suite.py:11(_call_if_exists)
        6    0.000    0.000    0.000    0.000 suite.py:142(_handleClassSetUp)
        8    0.000    0.000    0.000    0.000 suite.py:188(_get_previous_module)
        6    0.000    0.000    0.000    0.000 suite.py:196(_handleModuleFixture)
        1    0.000    0.000    0.000    0.000 suite.py:21(__init__)
        2    0.000    0.000    0.000    0.000 suite.py:250(_handleModuleTearDown)
        7    0.000    0.000    0.000    0.000 suite.py:285(_tearDownPreviousClass)
        1    0.000    0.000    0.000    0.000 suite.py:34(__iter__)
        6    0.000    0.000    0.000    0.000 suite.py:366(_isnotsuite)
        6    0.000    0.000    0.000    0.000 suite.py:44(addTest)
        1    0.000    0.000    0.000    0.000 suite.py:54(addTests)
        6    0.000    0.000    0.000    0.000 suite.py:69(_removeTestAtIndex)
        1    0.000    0.000    0.013    0.013 suite.py:83(__call__)
        4    0.000    0.000    0.000    0.000 take.py:121(_take_nd_ndarray)
        1    0.000    0.000    0.000    0.000 take.py:288(_get_take_nd_function_cached)
        4    0.000    0.000    0.000    0.000 take.py:326(_get_take_nd_function)
        4    0.000    0.000    0.000    0.000 take.py:565(_take_preprocess_indexer_and_fill_value)
        4    0.000    0.000    0.000    0.000 take.py:59(take_nd)
       29    0.000    0.000    0.000    0.000 textwrap.py:470(indent)
       93    0.000    0.000    0.000    0.000 textwrap.py:482(prefixed_lines)
        5    0.000    0.000    0.000    0.000 tokenize.py:299(detect_encoding)
        6    0.000    0.000    0.000    0.000 tokenize.py:323(read_or_stop)
        6    0.000    0.000    0.000    0.000 tokenize.py:329(find_cookie)
        5    0.000    0.000    0.000    0.000 tokenize.py:392(open)
        5    0.000    0.000    0.000    0.000 traceback.py:165(_format_final_exc_line)
       10    0.000    0.000    0.000    0.000 traceback.py:173(_safe_string)
       19    0.000    0.000    0.000    0.000 traceback.py:264(__init__)
       76    0.000    0.000    0.000    0.000 traceback.py:310(_original_line)
      171    0.000    0.000    0.002    0.000 traceback.py:316(line)
       24    0.000    0.000    0.000    0.000 traceback.py:349(_walk_tb_with_full_positions)
       19    0.000    0.000    0.000    0.000 traceback.py:363(_get_code_position)
        5    0.000    0.000    0.003    0.001 traceback.py:397(_extract_from_extended_frame_gen)
       19    0.000    0.000    0.001    0.000 traceback.py:458(format_frame_summary)
        5    0.000    0.000    0.001    0.000 traceback.py:513(format)
       38    0.000    0.000    0.000    0.000 traceback.py:561(_byte_offset_to_character_offset)
       19    0.000    0.000    0.000    0.000 traceback.py:577(_extract_caret_anchors_from_line_segment)
        5    0.000    0.000    0.000    0.000 traceback.py:616(__init__)
       15    0.000    0.000    0.000    0.000 traceback.py:621(indent)
       44    0.000    0.000    0.000    0.000 traceback.py:624(emit)
        5    0.000    0.000    0.000    0.000 traceback.py:632(<lambda>)
       59    0.000    0.000    0.000    0.000 traceback.py:635(<lambda>)
        5    0.000    0.000    0.003    0.001 traceback.py:675(__init__)
        5    0.000    0.000    0.000    0.000 traceback.py:790(_load_lines)
       10    0.000    0.000    0.000    0.000 traceback.py:803(format_exception_only)
       34    0.000    0.000    0.001    0.000 traceback.py:874(format)
      125    0.000    0.000    0.000    0.000 typing.py:2214(cast)
        5    0.000    0.000    0.000    0.000 util.py:115(three_way_cmp)
        1    0.000    0.000    0.000    0.000 util.py:24(_common_shorten_repr)
        2    0.000    0.000    0.000    0.000 util.py:45(safe_repr)
        5    0.000    0.000    0.000    0.000 util.py:54(strclass)
        2    0.000    0.000    0.000    0.000 utils.py:239(maybe_convert_indices)
        2    0.000    0.000    0.000    0.000 utils.py:62(is_list_like_indexer)
        3    0.000    0.000    0.000    0.000 warnings.py:440(__init__)
        3    0.000    0.000    0.000    0.000 warnings.py:466(__enter__)
        3    0.000    0.000    0.000    0.000 warnings.py:487(__exit__)
        1    0.000    0.000    0.000    0.000 weakref.py:369(remove)
        1    0.000    0.000    0.000    0.000 weakref.py:427(__setitem__)
       77    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF9F3999F90}
      104    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
     20/7    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       82    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _functools.cmp_to_key}
        1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        6    0.000    0.000    0.000    0.000 {built-in method _warnings._filters_mutated}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.all}
      173    0.000    0.000    0.000    0.000 {built-in method builtins.callable}
       19    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.dir}
        1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
     1576    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       63    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
       38    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
       14    0.000    0.000    0.000    0.000 {built-in method builtins.id}
2116/2112    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      128    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
       19    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
  846/754    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       38    0.000    0.000    0.000    0.000 {built-in method builtins.min}
    81/57    0.000    0.000    0.003    0.000 {built-in method builtins.next}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
       18    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.round}
      474    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        5    0.000    0.000    0.000    0.000 {built-in method io.open}
       16    0.001    0.000    0.001    0.000 {built-in method nt.stat}
       12    0.000    0.000    0.000    0.000 {built-in method numpy.array}
    60/58    0.000    0.000    0.000    0.000 {built-in method numpy.asarray}
       57    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
      102    0.000    0.000    0.000    0.000 {built-in method numpy.empty}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       17    0.000    0.000    0.000    0.000 {built-in method sys.exc_info}
        2    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
       68    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       29    0.000    0.000    0.000    0.000 {method '__contains__' of 'set' objects}
        5    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        5    0.000    0.000    0.000    0.000 {method '_rebuild_blknos_and_blklocs' of 'pandas._libs.internals.BlockManager' objects}
       25    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       12    0.000    0.000    0.000    0.000 {method 'add_index_reference' of 'pandas._libs.internals.BlockValuesRefs' objects}
        4    0.000    0.000    0.000    0.000 {method 'any' of 'numpy.ndarray' objects}
        6    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
      588    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'clear_mapping' of 'pandas._libs.index.IndexEngine' objects}
       19    0.000    0.000    0.000    0.000 {method 'co_positions' of 'code' objects}
        2    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}
       44    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       38    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        8    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
       13    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       40    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
      989    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 {method 'get_loc' of 'pandas._libs.index.IndexEngine' objects}
        2    0.000    0.000    0.000    0.000 {method 'getvalue' of '_io.StringIO' objects}
       12    0.000    0.000    0.000    0.000 {method 'groupdict' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
      134    0.000    0.000    0.000    0.000 {method 'isspace' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
    59/57    0.000    0.000    0.001    0.000 {method 'join' of 'str' objects}
        8    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       19    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
       23    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        2    0.000    0.000    0.000    0.000 {method 'max' of 'numpy.ndarray' objects}
        2    0.000    0.000    0.000    0.000 {method 'nonzero' of 'numpy.ndarray' objects}
        6    0.000    0.000    0.000    0.000 {method 'pop' of 'collections.deque' objects}
       66    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       33    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        6    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        5    0.001    0.000    0.001    0.000 {method 'readlines' of '_io._IOBase' objects}
       20    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        2    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
       69    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       18    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       31    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
      146    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
      190    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        7    0.000    0.000    0.000    0.000 {method 'sum' of 'numpy.ndarray' objects}
       10    0.000    0.000    0.005    0.001 {method 'throw' of 'generator' objects}
        6    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {method 'values' of 'mappingproxy' objects}
        2    0.000    0.000    0.000    0.000 {method 'write' of '_io.StringIO' objects}
       55    0.008    0.000    0.008    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        6    0.000    0.000    0.000    0.000 {pandas._libs.algos.ensure_platform_int}
        4    0.000    0.000    0.000    0.000 {pandas._libs.algos.take_1d_int64_int64}
        2    0.000    0.000    0.000    0.000 {pandas._libs.internals.get_blkno_placements}
       11    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_bool}
       29    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_float}
       22    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_integer}
       17    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_iterator}
       76    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_list_like}
       32    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_np_dtype}
       10    0.000    0.000    0.000    0.000 {pandas._libs.lib.is_scalar}
       11    0.000    0.000    0.000    0.000 {pandas._libs.lib.item_from_zerodim}
       50    0.000    0.000    0.000    0.000 {pandas._libs.lib.maybe_convert_objects}
        2    0.000    0.000    0.000    0.000 {pandas._libs.lib.maybe_indices_to_slice}
```