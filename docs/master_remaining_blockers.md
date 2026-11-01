# Remaining scientific dependencies

The master investigation improves the executable references but does not complete
the original predictive annealing study. The following dependencies are ordered
by their physical and computational use, not by document stage.

1. **Printed material state.** Identify a single formulation, pigment, print
   architecture, aging history and initial geometry. Obtain directional free
   recovery histories at multiple supported temperatures and durations, with
   heating/cooling part temperatures. Chapuis's active-road bilayer calibration
   does not identify the thickness or through-thickness state of a homogeneous
   60 mm × 10 mm × 4 mm coupon. Suder's reserved final means cannot identify
   rate and saturation independently. New characterization or a genuinely
   complete compatible published dataset is required.
2. **Thermal closure.** Compatible printed-state conductivity and heat capacity,
   density/use convention, convection and fixture heat-transfer conditions remain
   absent. A measured part-temperature history could permit a narrower structural
   reproduction, but would not validate an oven-to-part model. No cross-grade
   numerical patch is admissible as a measured Prusament property.
3. **Fixture and observation.** Specify the actual spacer/plate support path,
   hot clearance, compliance, surface condition, friction and contact transport.
   Select release time and the post-release observation interval. The new screen
   shows that different mounts can reverse the contact outcome. It does not
   establish which mount represents an existing experiment.
4. **Production implementation.** Assemble the supported initialized material law,
   thermal solution and distributed 3-D surface contact. The programmed recovery
   calculation is currently scalar Python; it is not a production ANSYS material
   implementation. The three stop cases are single-brick elastic limits. A
   physically supported bending mechanism is needed before interpreting warpage.
5. **Production verification and validation.** Refine mesh, time and contact on
   that full model. Preserve the reserved validation datasets independently of
   calibration. Reproduce measurable dimensions/shape under matched conditions;
   report deviations and uncertainty. Shape agreement alone does not validate
   residual stress or pressure. No physical validation error exists currently.
6. **Campaign and analysis.** Only after these prerequisites, freeze an admitted
   FREE/GAP design and run it. Process-variable sensitivity, material uncertainty,
   surrogate validation, Pareto analysis and independent solver confirmation all
   depend on actual eligible production data. There are zero approved or completed
   production cases, not a completed campaign with zero response.

The supported characterization interval is 23–85 °C; it is not a validated
annealing interval for arbitrary holds. Extending to 95 or 110 °C is rejected.
Alternative Black Devil Design or Ultrafuse data were investigated, but neither
provided the full compatible time/history/fixture evidence needed here. Restricting
the domain is therefore credible for verification, not a solution to all missing
physical inputs. These requirements cannot be met by additional benchmark runs,
more manuscript prose, or a numerical optimizer.
